\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{bsc}[2015/07/22 Style for my bachelor thesis]

\newif\if@print
\DeclareOption{print}{\@printtrue}
\DeclareOption{digital}{\@printfalse}

\ProcessOptions\relax


% General
\LoadClass[12pt,parskip=half]{scrreprt}

% Language
\usepackage[ngerman,english]{babel} % all languages being used, with main language last in list

% Geometry
\usepackage[onehalfspacing]{setspace}
\usepackage[a4paper,width=155mm,top=30mm,bottom=30mm]{geometry}

% Links
\usepackage{color,xcolor}
\usepackage{hyperref}
\if@print % switch link coloring off for printing
	\hypersetup{colorlinks=false}
\else
	\hypersetup{colorlinks=true}
\fi
\definecolor{uhd}{RGB}{196,19,47} % the red UHD brand color
\hypersetup{
	allcolors=uhd
}
\AtBeginDocument{
	\hypersetup{ % set pdf metadata
	    pdfauthor={\@author},
		pdftitle={\@title}
	}
}
\newcommand{\namedeqref}[2]{\hyperref[#2]{#1}~\eqref{#2}} % macro to reference equations by name
\newcommand{\appref}[1]{\hyperref[#1]{Appendix~\ref{#1}}} % macro to print appendix references

% Fonts
\usepackage{fontspec,xunicode}
\setmainfont{Palatino}
\setsansfont{Optima}
\setmonofont[Scale=MatchLowercase]{Menlo}

% Equations
\newcommand{\eqpunct}[1]{\mathpunct{#1}} % embed punctuation in equations
\newcommand{\eqname}[2]{\label{#2} \\[-1em] \tag*{\llap{\emph{#1}}}} % print a title for the equation

% Units
\usepackage{siunitx}
\DeclareSIUnit\parsec{pc}
\sisetup{
	separate-uncertainty = true
}

% Images
\usepackage{pgf}
\newcommand{\plt}[3]{
	\begin{figure}[h]
		\begin{center}
			\input{plots/#1.pgf}
		\end{center}
		\caption[#2]{\textbf{#2} \quad #3}
		\label{fig:#1}
	\end{figure}
}

% Tables
\usepackage{array} % for math mode in tables
\usepackage{booktabs} % for hline rules

% Quotations
\usepackage{epigraph}
\setlength{\epigraphwidth}{.8\textwidth}
\setlength{\epigraphrule}{0pt}

% Paging animation
\usepackage{pageslts}
\newcommand{\vcenteredicon}{
	\begingroup
	\setbox0=\hbox{
		\scalebox{0.2}{
			\if@twoside
				\input{paging_animation/alternating_\theCurrentPage.pgf}
			\else
				\input{paging_animation/continuous_\theCurrentPage.pgf}
			\fi
	    }
	}\parbox{\wd0}{\box0}
	\endgroup
}

% Page Layout
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\if@print
	\fancyhead[LE]{
	    \textit{\nouppercase{\leftmark}}
	}
	\fancyhead[RO]{
		\textit{\nouppercase{\rightmark}}
	}
	\fancyfoot[RO]{
		\vcenteredicon{} \thepage
	}
	\fancyfoot[LE]{
		\thepage \vcenteredicon{}
	}
\else
	\fancyhead[L]{
	    \textit{\nouppercase{\leftmark}}
	}
	\fancyfoot[C]{
		\vcenteredicon{} \thepage
	}
\fi
\renewcommand{\headrulewidth}{0.2pt}

\fancypagestyle{plain}{%
	\fancyhf{}
	\if@print
		\fancyfoot[RO]{
			\vcenteredicon{} \thepage
		}
		\fancyfoot[LE]{
			\thepage \vcenteredicon{}
		}
	\else
		\fancyfoot[C]{
			\vcenteredicon{} \thepage
		}
	\fi
	\renewcommand{\headrulewidth}{0pt}
	\renewcommand{\footrulewidth}{0pt}
}


% Bibliography
\usepackage[style=numeric-comp, backend=biber, maxnames=10, maxcitenames=2]{biblatex}
%\nocite{*} % print all references, even those not used

% Appendix
\usepackage[toc,page]{appendix}


\endinput
