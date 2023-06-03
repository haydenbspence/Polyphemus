# Polyphemus

Polyphemus is a collection of specialty trained Large Language Models (LLMs) for use in applications to support observational health informatics and data science. 

## Introduction

The main goal of Polyphemus is to provide a collection of LLMs that are localized to functional areas. We use a varient of the village analogy in the paper [*Generative Agents: Interactive Simulacra of Human Behavior*](file:///C:/Users/diana/Downloads/2304.03442.pdf) to describe our methodology.
Instead of a village, we draw the analogy to a Research Park where each fine-tuned LLM is an individual researcher in the park. Each of their qualities are described as well as how they interact to solve complex research challenges.

## Table of contents

1. List of Abbreviations
2. Abstract
3. Amendments and Updates
4. Roadmap

## List of Abbreviations

OHDSI - Observational Health Data Sciences and Informatics

OMOP - Observational Medical Outcomes Partnership

AI - Artificial Intelligence

LLaMA - Large Language Model Meta AI

fLLM - Foundational Large Language Model

LLM - Large Language Model

API - Application Program Interface

SOTA - State of the Art

RLHF - Real Life Human Feedback

PALM - Pretrained Autoencoding Language Model

GPT - Generative Pretrained Transformer

MWE - Minimum Working Example

MRE - Minimum Reproducible Example

MVP - Minimum Viable Product

## Abstract

The Observational Medical Outcomes Partnership (OMOP) is strategically positioned to profoundly influence the application of artificial intelligence (AI) to open science and observational medical research. An internal Google document leaked in early May 2023 underscores the potential of Open Source AI to outperform major technology firms in the sector. Open source and open science possess significant advantages over private entities and institutions, primarily the capability to organically set standards, foster collaboration, and enhance interoperability. The Polyphemus Project is an innovative proposal aimed at replicating and tailoring cutting-edge advancements in Open Source AI to suit the needs of observational medical research. By establishing comprehensive frameworks, offering educational materials, conducting evaluations, and providing infrastructural access, the project aspires to facilitate and encourage the integration and development of open-source AI tools and methodologies within the OHDSI community. This approach stands to democratize AI, advancing the field while bolstering the quality and inclusivity of observational medical research.

## Amendments and Updates

## Milestones

- **Initial Charter and Organizational Documents**
  - Define the mission, vision, and core values of The Polyphemus Project.
  - Outline the overall objectives, deliverables, and milestones for the project.
  - Set up the project governance structure and decision-making protocols.
  - Establish a clear plan for communication, including the frequency and formats of meetings, publications, and presentations.
  - Identify key roles and responsibilities within the project.

- **Infrastructure Planning and Funding Strategies**
  - Identify the necessary hardware and software requirements for project execution.
  - Establish partnerships and collaborations with other institutions and organizations for resource sharing.
  - Develop a detailed budget and identify potential sources of funding, including grants, sponsorships, and donations.
  - Apply for funding and manage the disbursement of funds efficiently.

- **Minimal Working Example (MWE): Initial Model Prototype(s) and Evaluation(s)**
  - Develop an initial prototype of the AI models for observational medical research based on open-source tools and methods.
  - Perform preliminary evaluations to assess the performance and accuracy of the models.
  - Make necessary adjustments based on the evaluation results.

- **Broad Community Engagement in Data Collection**
  - Initiate collaborations with institutions and organizations for data collection.
  - Ensure ethical guidelines and standards are followed during data collection and management.
  - Start community-engagement initiatives to increase awareness and participation in the project.

- **Minimal Reproducible Example (MRE) for Larger Community Collaboration and Evaluation**
  - Develop a more refined and reproducible example of the AI models that other researchers can test and evaluate.
  - Organize workshops and training sessions to help community members understand and utilize the MRE.

- **Publications and Presentations**
  - Regularly update the community about project progress through publications and presentations.
  - Publish research findings in peer-reviewed journals and present at relevant conferences.
  - Ensure open and transparent communication about the project's progress, challenges, and success stories.

- **Minimal Viable Product (MVP) for OHDSI Community Use**
  - Finalize a functional and effective AI tool for observational medical research that meets the needs of the OHDSI community.
  - Conduct rigorous testing and evaluation to ensure the MVP meets the desired standards of accuracy and usability.
  - Provide comprehensive documentation and user support for the MVP.
  - Plan for the long-term sustainability and scalability of the MVP, including updates, maintenance, and user support.


## Rationale and Background

### Recent Developments in Open Source Large Language Models
On March 3, 2023, a significant event occurred in the field of artificial intelligence. Meta's Large Language Model Meta AI (LLaMA) was leaked and subsequently shared via a torrent file on the internet. This foundational large language model (fLLM) spurred a rapid proliferation of open source projects. Unlike its counterparts, such as OpenAI's GPT4 and Google's PaLM2, LLaMA became freely accessible rather than being locked behind authorized web-applications or application program interfaces (APIs). In a noteworthy example of the model's accessibility, the smaller 7B parameter version was successfully [deployed on a Raspberry Pi by Artem Andreenko](https://github.com/ggerganov/llama.cpp/issues/58).

A few days later, on March 13, [researchers from Stanford fine-tuned the 7B LLaMA model](https://crfm.stanford.edu/2023/03/13/alpaca.html) using a technique known as Self-Instruct[^3]. They [open-sourced the instructions](https://arxiv.org/abs/2212.10560), thereby creating a model that was trained for both instruction and conversation. Following the publication of LLaMA's code, Eric Wang released Alpaca-LoRA, a reproduction of Stanford's Alpaca utilizing low-rank adaptation (LoRA)[^4]. Alpaca-LoRA made it possible for consumer hardware to reproduce Stanford's methods. As a result, anyone with a high-performance gaming computer or a modest cloud computing budget could train their own generalized or specialized LLaMA-derived model. The potential implications of these developments are far-reaching, to say the least. Continued performance enhancements by Georgi Gerganov [using 4-bit quantization](https://github.com/ggerganov/llama.cpp) even made it feasible to run LLaMA using only a CPU.

## Objectives

### Primary Objectives

- **Objective 1:** Foster a transparent and collaborative culture within the Observational Medical Outcomes Partnership (OMOP) to optimally utilize artificial intelligence (AI) in open science and observational medical research.

- **Objective 2:** Streamline the integration of AI and Large Language Models (LLMs) into OMOP's framework to enhance data processing capabilities, ultimately striving for increasing the iteration speed of research and development.

- **Objective 3:** Advocate for the adoption of LLMs and AI into open-source platforms, aiming to lower the entry barriers for smaller organizations and individuals, thereby stimulating diversity in the AI technology landscape.

- **Objective 4:** Facilitate the adoption of open-source AI tools within OMOP to amplify the reproducibility and transparency of research findings and data processing methodologies.

- **Objective 5:** Champion the democratization of LLMs and AI through open-source initiatives, empowering individuals and smaller organizations to innovate, thereby cultivating a more inclusive technological landscape.

- **Objective 6:** Promote the use of open-source AI tools and frameworks within OMOP to expedite the development of novel methodologies and analytical techniques for processing large-scale healthcare data. Progress can be assessed by tracking the pace of methodological innovations and enhancements in large-scale data analysis.

### Design


## Data Storage
- JSON
- Duckdb
- Pandas

## Data Source(s)

- OMOP CDM v5.4

