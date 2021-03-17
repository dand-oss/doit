# lazy way to ignore coverage in this file
if True:  # pragma: no cover
    import sys

    def main(argv=None):
        if not argv:
            argv = sys.argv[1:0]

        from doit.doit_cmd import DoitMain

        return DoitMain().run(argv)

    if __name__ == '__main__':
        sys.exit(main())
