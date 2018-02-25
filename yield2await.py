import argparse
import ast

import astor

parser = argparse.ArgumentParser()
parser.add_argument('path')
parser.add_argument('-i', '--ignore')


class Transformer(ast.NodeTransformer):

    def visit_YieldFrom(self, node):
        return ast.Await(node.value)

    def visit_With(self, node):
        change_node = False
        new_items = []
        for item in node.items:
            if isinstance(item.context_expr, ast.YieldFrom):
                new_item = ast.withitem(
                    item.context_expr.value,
                    item.optional_vars,
                )
                new_items.append(new_item)
                change_node = True
            else:
                new_items.append(item)

        if not change_node:
            return node

        return ast.AsyncWith(items=new_items, body=node.body)

    def visit_FunctionDef(self, node):
        change_node = False
        decorator_list = []
        for decorator in node.decorator_list:
            if (
                isinstance(decorator, ast.Attribute) and
                decorator.value.id == 'asyncio' and
                decorator.attr == 'coroutine'
            ):
                change_node = True
            else:
                decorator_list.append(decorator.id)

        if not change_node:
            return node

        return ast.AsyncFunctionDef(
            name=node.name,
            args=node.args,
            body=node.body,
            decorator_list=decorator_list,
            returns=node.returns,
        )


def transform(path, transformer):
    with open(path) as f:
        source = f.read()

    tree = ast.parse(source)
    old_tree_dump = astor.dump_tree(tree)

    transformer.visit(tree)
    transformer.visit(tree)
    transformer.visit(tree)

    if old_tree_dump == astor.dump_tree(tree):
        return

    source = astor.to_source(tree)

    with open(path, 'w') as f:
        f.write(source)


def main():
    args = parser.parse_args()

    transformer = Transformer()
    files = astor.code_to_ast.find_py_files(
        args.path, ignore=args.ignore)

    for _, path in files:
        print(path)
        transform(path, transformer)

    print('Done!')


if __name__ == '__main__':
    main()
