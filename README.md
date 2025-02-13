# ac3-book - Gateway to the (AC)³ research project on Arctic amplification

[Latest build](https://ac3-tr.github.io/ac3-book/)

This repository holds a [jupyter book (version 2)](https://next.jupyterbook.org/) with 

- background information
- data descriptions
- example use cases

about and from the Transregional Collaborative Research Centre (TRR 172) on Arctic Amplification: Climate Relevant Atmospheric and Surface Processes, and Feedback Mechanisms (AC)³ (2015 - 2027).

This book is being build as a place of exchange for researches inside and outside the (AC)³ project. It should help you learn more about our research results and quickly find the data, on which we based our results.

## Roadmap

- [ ] Develop structure of the book
- [ ] Incorporate [ac3-notebooks](xref:ac3notebooks) and [ac3airborne](xref:ac3airborne)
- [ ] Develop a template to provide members to add example notebooks showcasing the use of some data
- [ ] Link each example notebook to the platform(s) and data source(s) it uses
- [ ] List all example notebooks on the page of the respective platform(s) that created the data for it
- [ ] Port information from the website to the book
- [ ] Port information from campaign wikis and websites to the book

## Contribute

Help to grow this project by raising an issue ~~or suggesting an edit directly at one of the book pages~~ (to be implemented by the mystmd book theme).
You can also open a pull request if you want to add more example notebooks.

### Local Setup

"Jupyter Book 2 is a very thin wrapper around the MyST-MD engine: it shares the same CLI and configuration file. It serves primarily as an introduction of the existing Jupyter Book community to the MyST-MD engine.
If you're new to the Jupyter Book project, consider [directly using MyST-MD](https://mystmd.org/guide/quickstart)." (from [next.jupyterbook.org](https://next.jupyterbook.org/start/install))

We follow this advice in the description below.

Here's how to set up the ac3-book book for local development.

1. [Fork the repo](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks) on GitHub.
2. Clone your fork locally.
3. Create a python environment with all dependencies, e.g., by using `conda`: `conda env create -f environment.yml`
4. [Create a branch](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) for local development and make changes locally. See the [mystmd guide](https://mystmd.org/guide) for help on syntax.
5. Build the book locally to see if the fully-rendered HTML version looks as intended.
   ```sh
   cd book  # change into the book directory
   myst start  # start your local webserver
   ```
6. Commit your changes and push your branch to your fork on GitHub.
7. [Create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) through the GitHub website.

## References and Inspiration

- [How to EUREC4A](https://howto.eurec4a.eu/intro.html)
- [How to ac3airborne](https://igmk.github.io/how_to_ac3airborne/intro.html)
- [Orcestra](https://orcestra-campaign.org/intro.html)
- [jupyter book v2](https://next.jupyterbook.org/)
- [MystMD](https://mystmd.org/)

## License

 Content in the ac3-book © 2025 by the Transregional Collaborative Research Centre 172 (AC)³ is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1)
 
Code within this repository is licensed under [MIT](https://opensource.org/license/MIT).