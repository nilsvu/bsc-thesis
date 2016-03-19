# Bachelor Thesis in Physics

- **Title:** Gravitational Waves in Modified Gravity
- **Author:** Nils Fischer
- **Supervisors:** [Dr. Valeria Pettorino](https://valeriapettorino.wordpress.com) and [Prof. Dr. Luca Amendola](https://lucaamendola.wordpress.com)
- **Institution:** [Institute for Theoretical Physics, Department of Physics and Astronomy, University of Heidelberg](http://www.thphys.uni-heidelberg.de)
- **Abstract:** Modified gravity theories generally aim to solve part of the *cosmological constant problem* by providing self-accelerating cosmological solutions without a cosmological constant. Such modifications of general relativity also affect the evolution of gravitational waves in the proposed theory. Instead of focussing on an explicit model, I introduce parametric modifications to the evolution equation of gravitational waves in both unimetric and bimetric settings and investigate their effect on the evolution of tensor perturbation modes. In particular, I argue that any modified gravity theory that exhibits *growing tensor modes* in cosmological evolution can be in tension with experiments. Therefore, parametric constraints for the physical viability of a general modified gravity theory can be found such that tensor modes remain within limits set by observations.
- **Full Text:** [Digital Version](https://github.com/knly/bsc-thesis/blob/master/dist/bsc_digital.pdf) | [Onesided Print Version](https://github.com/knly/bsc-thesis/blob/master/dist/bsc_oneside.pdf) | [Twosided Print Version](https://github.com/knly/bsc-thesis/blob/master/dist/bsc_twoside.pdf)


## Using the LaTeX style for your thesis

- Just drop the `bsc.cls` file into your project folder and begin your document with `\documentclass{bsc}`. See the `bsc.tex` file for an example. Then, you can adjust everything in the `bsc.cls` file to your needs.

- Typeset the document with the [XeLaTeX](http://www.xelatex.org/) typesetting engine and the [Biber](http://biblatex-biber.sourceforge.net) bibliography processor (recommended).

- Adjust the following `documentclass` options to produce appropriate digital and print versions of the document:

	- `digital` / `print` toggles e.g. link coloring and page number positioning
	- `oneside` / `twoside` according to print layout
	- `openright` / `openleft` / `openany` adjusts positioning of title page and chapter beginnings in twosided layout

- If necessary for binding, adjust the page offset:

	```tex
	\geometry{
		bindingoffset=5mm,
	}
	```

- You may need to change the fonts specified in `bsc.cls` to ones installed on your system.

- When you include plots in your document, use vector file formats instead of pixel graphics. Have a look at my [TexFig](https://github.com/knly/texfig) repository to see how to generate PGF vector plots with Python's Matplotlib that look great in your LaTeX document.
