.PHONY: build clean build-test build-sol-test build-types-test clean-test build-example build-sol-example build-types-example clean-example

build:
	make build-test
	make build-example

clean:
	make clean-test
	make clean-example

build-test:
	make build-sol-test
	make build-types-test

build-sol-test:
	sh scripts/build_sol_test.sh	
	python scripts/format_json_dir_test.py

build-types-test:
	sh scripts/generate_types_test.sh

clean-test:
	rm -rf rm -rf pypechain/test/*/abis/* && rm -rf pypechain/test/*/types/*

build-example:
	make build-sol-example
	make build-types-example

build-sol-example:
	sh scripts/build_sol_example.sh	
	python scripts/format_json_dir_example.py

build-types-example:
	sh scripts/generate_types_example.sh

clean-example:
	rm -rf example/abis/* && rm -rf example/types/*



