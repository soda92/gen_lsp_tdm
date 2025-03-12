all: build

.PHONY: build

build:
	cmake --preset windows
	cmake --build build
	gen_lsp_tdm

clean:
	pwsh -nop -c "rm -r -Force build"
