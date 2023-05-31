# Polyphemus

Polyphemus is a network of specialty trained LLMs for use in applications to support observational medical research.

## Introduction

The infamous Cyclops, Polyphemus, the son of Poseidon in Greek mythology, met his downfall due to the cunning of the hero, Odysseus. When asked for his name, Odysseus cleverly responded with 'Nobody.' Unable to pinpoint the culprit behind his blinding, Polyphemus could not seek revenge, his actions limited to hurling a boulder aimlessly into the sea. It wasn't until Odysseus revealed his true name that the cyclops was able to enlist his father Poseidon's divine wrath, highlighting the power of a name.

Similarly, in the world of systems integration, the naming of objects is crucial. Each object must have a consistent name across various systems. While the characteristics of the object might change over space and time, the name serves as a constant identifier. With a proper name, actions can be directed effectively, whereas without it, one can only attempt hit-or-miss strategies.

The importance of naming extends to the realm of artificial intelligence (AI) systems. Large Language Models (LLMs) such as GPT-3, the driving force behind ChatGPT and OpenAI's API, exemplify this. These models can perform tasks but lack the ability to recognize specific names within specialized knowledge domains. This limitation hampers their wider application, especially in fields such as observational medical research.

Introducing Polyphemus, a network of specialty-trained Large Language Models (LLMs), designed to overcome this limitation. Polyphemus models can not only act but also identify object names within their specialized domain. This project, a collaborative effort between the Observational Health Data Sciences and Informatics (OHDSI) community and Polyphemus, focuses on the exploration of LLMs' application in open science and observational medical research.

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

*As of mid-March, open-source and open science projects were starting to gain momentum:*

- **March 19**: The [Vicuna](https://lmsys.org/blog/2023-03-30-vicuna/) project trained the model on high-quality ChatGPT dialogues sourced from sites such as [ShareGPT](https://sharegpt.com/). The training cost was approximately $400.
- **March 25**: [GPT4ALL](https://github.com/nomic-ai/gpt4all) trained a model and implemented the first ecosystem that unites other models like Vicuna in a single location. The training cost was around $100.
- **March 28**: [Cerebras](https://www.cerebras.net/) trained the GPT-3 architecture using the optimal compute schedule implied by Chinchilla and the optimal scaling implied by [μ-parameterization](https://arxiv.org/abs/2203.03466). This marked the first example of a model that outperformed GPT-3 and was trained from scratch. Consequently, the open source community gained full access to two fLLMs that rival GPT4 and PaLM2.
- **March 28**: The [LLaMA-Adapter](https://arxiv.org/pdf/2303.16199.pdf) project introduced instruction tuning and multimodality in a mere hour of training, establishing a new state-of-the-art (SOTA) for Science Q&A.
- **April 3**: The [Koala](https://bair.berkeley.edu/blog/2023/04/03/koala/) project released a model trained on open source data. When evaluated against ChatGPT with human subjects, over 50% of users either preferred Koala responses or expressed no preference between the two. The training cost was approximately $100.
- **April 15**: The [Open Assistant Conversations](https://drive.google.com/file/d/10iR5hKwFqAKhL3umx8muOWSRm7hs5FqX/view) project launched a model and dataset for Alignment via Real Life Human Feedback (RLHF). Their model closely competed with ChatGPT in terms of human preference (48.3% vs. 51.7%). The dataset could also be applied to Pythia-12B, and a complete open-source technology stack was provided to run the model. This publicly available dataset made RLHF feasible for individual users. 

### The Era of Democratized AI: Developments Since April 15th

After April 15, the trend of democratizing AI continues to accelerate. The following are some of the most notable developments in the field of open-source AI since then:

- [LangChain](https://github.com/hwchase17/langchain) - A library to assist in the development of data-aware agentic LLM applications by including multiple LLMs combined with other sources of information. Examples include Q&A over specific documents, databases, or APIs; chatbots that can reason before responding; agents that have control over system environments to perform tasks.
  - [Chain of Thought (CoT)](https://arxiv.org/pdf/2201.11903.pdf) / [Step-by-Step](https://arxiv.org/abs/2112.00114) - a prompting technique used to encourage the model to generate a series of intermediate reasoning steps.
  - Action Plan Generation ([WebGPT](https://arxiv.org/pdf/2112.09332.pdf) - [SayCan](https://say-can.github.io/assets/palm_saycan.pdf)), a prompting technique that uses a language model to generate actions to take. The results of these actions can then be fed back into the language model to generate a subsequent action.
  - [ReAct](https://arxiv.org/pdf/2210.03629.pdf) - a prompting technique that combines Chain-of-Thought prompting with action plan generation. This induces the model to think about what action to take, then take it.
  - [More concepts from LangChain documentation](https://python.langchain.com/en/latest/getting_started/concepts.html)

- [LlamaIndex](https://github.com/jerryjliu/llama_index) - a comprehensive data framework that enhances LLMs and allows users to incorporate their private data effectively. Users can connect their existing data sources and formats easily. LlamaIndex also offers an advanced retrieval and query interface for retrieving context and augmenting knowledge-based output.

- [GPTCache](https://github.com/zilliztech/GPTCache) - a semantic cache for storing LLM responses.

- [LocalAI](https://github.com/go-skynet/LocalAI) - a drop-in replacement REST API that's compatible with OpenAI API specifications for local inferencing.

- [PandasAI](https://github.com/gventuri/pandas-ai) - a Python library that adds generative artificial intelligence capabilities to Pandas.


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

