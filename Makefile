.PHONY: build build-test build-test-sol build-test-types clean

build-test:
	make build-test-sol
	make build-test-types
	make build-test-format-abi

build-test-sol:
	sh scripts/rebuild_sol.sh	

build-test-format-abi:
	python scripts/format_json_dir.py

build-test-types:
	sh scripts/regenerate_types.sh

clean:
	rm -rf example/abis/* && rm -rf example/types/* && rm -rf pypechain/test/*/abis/* && rm -rf pypechain/test/*/types/*



