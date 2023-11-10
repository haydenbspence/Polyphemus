# Contributing to Polyphemus

Contributions are welcome.

Active areas of development include the following:

- Documentation

- Data Collation and Quality Control

- Data Governance and AI Ethics

- Commond Data Model (CDM) and Vocabulary Support

- Front End Development and User Experience

- Infrastructure and DevOps

- Data Science and Machine Learning

- Evaluation and Testing

- Grants and Fundraising

- Partnerships and Collaboration

- Dissemination and Outreach

## Contribution Guidelines

Polyphemus follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/1/4/code-of-conduct.html). By contributing to the project you agree to abide by its terms.

### General Process
- Setup your development environment.
- Fork the repo and create your branch from `main`.
- If you've added code that should be tested, add tests.
- Ensure all tests pass.
- Submit a pull request.

For more information about the types of development environments, please see the [Development Environments](https://haydenbspence.github.io/Polyphemus/contributing/development-environments/)) section of the documentation.

We deliniate development environments based on the following categories:

- **[Standard Environment]()**:  This environment is for contributions to the source code of the Polyphemus library. It is primarily a Python development environment.

- **[Model Environments]()**:  Each model has its own development environment that is documented on a seperate repository. For more information, see the [Models](https://haydenbspence.github.io/Polyphemus/models/) page in the documentation.

- **[Deployment Environment]()**:  This environment is for contributions to the deployment of Polyphemus. It is primarily a DevOps environment.

- **[Documentation Environment]()**:  This environment is for contributions to the documentation of Polyphemus. It is primarily a [Quarto](https://quarto.org/) environment. 
<!--- - Sign the  [Contributor Agreement ("CLA")]().  -->

### Standard Development Environment

### Model Development Environment

- Install [Python](https://www.python.org/downloads/).
- Select from the Models which you would like to contribute to.
- https://haydenbspence.github.io/Polyphemus/models/

<!---  ### Contributor License Agreement

We ask that all contributors sign a Contributor License Agreement ("CLA"). This is to ensure that Polyphemus remains open source and free to use for everyone. The CLA is a short form that covers contributions to all Polyphemus projects. It is based on the [Apache Foundation CLA](https://www.apache.org/licenses/#clas) and [MongoDB CLA](https://www.mongodb.com/legal/contributor-agreement). -->

### Deployment Development Environment

<!--- TODO: Add Ansible + Teraform to automatically provision in cloud -->

A full deployment development environment requires the setup of a development cluster. This section is a work in progress.

- Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).
- Install [Vagrant](https://developer.hashicorp.com/vagrant/downloads) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads)


Alternatively, you can use local spare hardware and [Proxmox](https://www.proxmox.com/en/) or a cloud provider to setup a development cluster.

# Authorship and Acknowledgements

For academic publications and works, Polyphemus follows the [OHDSI Authorship Guidance](https://www.ohdsi.org/wp-content/uploads/2021/07/OHDSI-Authorship-Guidance.pdf), which follows the [ICMJE guidelines for authorship requirements](https://www.icmje.org/recommendations/). If a student is using Polyphemus for a thesis or dissertation, the student should be the first author.

Contributors that sign a [Contributor Agreement]() are included in acknowledgements using the [CRediT taxonomy](https://casrai.org/credit/).


## License
By contributing to Polyphemus, you agree that your contributions will be licensed
under the LICENSE file in the root directory of this source tree.