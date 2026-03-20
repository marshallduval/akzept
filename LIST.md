# akzept

> Seeded from `exports/aprt-snapshot-2026-03-20.json`.

Curated references for agentic provenance R&D.

## Contents

- [Agent Protocols](#agent-protocols)
- [Clinical Research](#clinical-research)
- [Content Provenance (C2PA)](#content-provenance-c2pa)
- [Cultural Heritage (CIDOC-CRM, IIIF)](#cultural-heritage-cidoc-crm-iiif)
- [Digital Preservation (OAIS)](#digital-preservation-oais)
- [Domain Applications](#domain-applications)
- [Governance & Standards Bodies](#governance-and-standards-bodies)
- [Infrastructure Projects](#infrastructure-projects)
- [Laboratory Science (ELN)](#laboratory-science-eln)
- [ORNL / SC'25 Cluster](#ornl-sc25-cluster)
- [Practitioner Evidence](#practitioner-evidence)
- [RO-Crate & Packaging](#ro-crate-and-packaging)
- [Reproducibility](#reproducibility)
- [Supply Chain (AIBOM)](#supply-chain-aibom)
- [Tools & Libraries](#tools-and-libraries)

## Agent Protocols

- [A2A Protocol (Agent-to-Agent) v1.0](https://a2aproject.org) - Agent-to-agent communication protocol. v1.0: TSC formalized (8 companies), JWS signatures, OAuth/PKCE, extensions array confirmed as provenance extension insertion point.
- [Agent Communication Protocol (ACP)](https://agentcommunicationprotocol.dev) - Agent communication protocol. Spec at github.com/agntcy/acp-spec.
- [Agent Network Protocol (ANP)](https://agentnetworkprotocol.com) - Protocol for agent networking and discovery.
- [Agora Protocol](https://agoraprotocol.org) - Agent communication protocol from University of Oxford. Semantic-web-grounded agent discovery and interaction.
- [IETF agent:// URI Scheme (draft-narvaneni-agent-uri)](https://datatracker.ietf.org/doc/draft-narvaneni-agent-uri/) - IETF Internet-Draft for agent:// URI scheme (v02, Oct 2025). See also draft-sogomonian-ai-uri-scheme.
- [Model Context Protocol (MCP) Specification](https://modelcontextprotocol.io) - Protocol for LLM-to-tool integration. Current spec Nov 2025. Session G: ecosystem fracture signal (Perplexity CTO departure, context window consumption issues).
- [SCIM for Agents (IETF draft-abbey-scim-agent-extension)](https://datatracker.ietf.org/doc/draft-abbey-scim-agent-extension/) - IETF draft extending SCIM 2.0 (RFC 7643) for agent identity.
- [W3C PROV-O (Provenance Ontology)](https://www.w3.org/TR/prov-o/) - W3C Recommendation (2013). Core ontology for provenance. Foundation for Gap 1-3 work in ARP project.

## Clinical Research

- [CONSORT-AI Reporting Guideline](https://www.consort-statement.org/consort-ai) - Reporting guideline for AI in clinical trials.
- [FAIR Guiding Principles](https://www.go-fair.org/fair-principles/) - Findable, Accessible, Interoperable, Reusable data principles.

## Content Provenance (C2PA)

- [AI4LAM / Fantastic Futures 2026 (Washington DC, Sep 14-18)](https://blogs.loc.gov/thesignal/2024/06/ai4lam-fantastic-futures/) - International AI for LAM conference. 2026 edition in Washington DC. AI4LAM forming as official membership org hosted by National Library of Norway.
- [C2PA for G+LAM Community Group (Library of Congress)](https://blogs.loc.gov/thesignal/2025/07/c2pa-glam/) - Library of Congress initiative for C2PA in galleries, libraries, archives, and museums. Founded January 2025.
- [C2PA Technical Specification v2.2](https://spec.c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html) - Current published version (May 1, 2025). v2.3 explainer available. Fast-tracked as ISO standard. Session H monitoring update.
- [C2PA Technical Specification v2.3](https://spec.c2pa.org/specifications/specifications/2.3/specs/C2PA_Specification.html) - Content provenance and authenticity standard. Active draft, December 2025.
- [c2pa-python (Content Authenticity SDK)](https://pypi.org/project/c2pa-python/) - Python SDK for C2PA content provenance.

## Cultural Heritage (CIDOC-CRM, IIIF)

- [CIDOC-CRM v7.3.2 (ISO 21127:2023)](https://cidoc-crm.org/Version/version-7.3.2) - Conceptual Reference Model for cultural heritage. Published March 2026. SIG meetings: Oxford (Mar 23-26), Nuremberg (Oct 6-9).
- [IIIF Consortium — International Image Interoperability Framework](https://iiif.io/) - 70-member global consortium. Presentation API v3 current, v4 release candidate (target June 2026).

## Digital Preservation (OAIS)

- [E-ARK Specifications (OAIS Implementation)](https://www.e-ark-foundation.eu) - European Archival Records and Knowledge Foundation.
- [OAIS Reference Model (ISO 14721:2025 / CCSDS 650.0-M-2)](https://public.ccsds.org/publications/archive/650x0m2.pdf) - Open Archival Information System reference model. ISO 14721:2025 (published Dec 2024). Foundation for Gap 5 (Designated Community mapping).
- [Records in Contexts Ontology (RiC-O)](https://www.ica.org/standards/ric/ontology) - International Council on Archives ontology for archival description. GitHub: ICA-EGAD/RiC-O.

## Domain Applications

- [A Study on the MCP × A2A Framework for Enhancing Interoperability](https://arxiv.org/abs/2506.01804) - Analysis of MCP and A2A protocol interoperability.
- [Agent-OSI Reference Architecture (arXiv:2602.13795)](https://arxiv.org/abs/2602.13795) - OSI-inspired layered reference architecture for AI agents.
- [Security Threat Modeling for Agent Protocols (arXiv:2602.11327)](https://arxiv.org/abs/2602.11327) - Security threat modeling for A2A and Agora protocols.
- [VASPilot: MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations](https://arxiv.org/abs/2508.07035) - MCP-facilitated multi-agent system for materials science (VASP simulations).

## Governance & Standards Bodies

- [Agentic AI Foundation (AAIF)](https://aaif.io) - Directed fund under Linux Foundation providing neutral governance for open-source agentic AI infrastructure. Founded December 9, 2025.
- [ORNL INTERSECT](https://www.ornl.gov/intersect) - Oak Ridge National Laboratory's open federated architecture for interconnected science ecosystems.
- [W3C WebAgents Community Group](https://www.w3.org/groups/cg/webagents/) - W3C community group for web-based agent standards.

## Infrastructure Projects

- [AGNTCY (Cisco/Linux Foundation)](https://agntcy.org) - Open-source agent infrastructure (35+ repos). Includes slim-otel, observe SDK covering all three protocol layers. Founded July 2025 under Linux Foundation.
- [OpenTelemetry GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) - CNCF OpenTelemetry semantic conventions for generative AI and agent spans. Key for Gap 3 (PROV-O to OTel mapping).

## Laboratory Science (ELN)

- [ELN Consortium — .eln File Format](https://github.com/TheELNConsortium/TheELNFileFormat) - Electronic Lab Notebook file format based on RO-Crate. IANA media type: application/vnd.eln+zip. Third independent RO-Crate convergence point (Gap 2).
- [protocols.io — Protocol Publication Platform](https://www.protocols.io) - Open platform for protocol publication and versioning. API at apidoc.protocols.io.
- [REPRODUCE-ME Ontology](https://w3id.org/Reproduce-ME) - PROV-O/P-Plan extension for experiment reproducibility. ProvBook tool for Jupyter notebook provenance. Near-tier provenance cluster.

## ORNL / SC'25 Cluster

- [A Grassroots Network and Community Roadmap for Interconnected Autonomous Science Laboratories](https://arxiv.org/abs/2506.17510) - Roadmap for interconnected autonomous science labs.
- [Empowering Scientific Workflows with Federated Agents](https://arxiv.org/abs/2505.05428) - Federated agent architecture for scientific workflows. Argonne/UChicago. Updated January 2026.
- [LLM Agents for Interactive Workflow Provenance: Reference Architecture and Evaluation Methodology](https://arxiv.org/abs/2509.13978) - Reference architecture for LLM agent workflow provenance. SC Workshops '25 (November 2025). v2 confirms MCP architecture.
- [Multimodal Provenance-Aware Defense Framework (arXiv:2512.23557)](https://arxiv.org/abs/2512.23557) - Defense against prompt injection in multi-agent systems using provenance-aware techniques.
- [PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions](https://arxiv.org/abs/2508.02866) - Unified provenance model for AI agent interactions. Accepted IEEE e-Science 2025.
- [The (R)evolution of Scientific Workflows in the Agentic AI Era](https://arxiv.org/abs/2509.09915) - Vision paper on scientific workflows and agentic AI.

## Practitioner Evidence

- [HN: 1M Context GA Discussion (2026-03-14)](https://news.ycombinator.com/item?id=47367129) - 41 substantive comments on context window scaling, agent infrastructure, and production deployment patterns.

## RO-Crate & Packaging

- [RO-Crate Specification](https://w3id.org/ro/crate) - Research Object Crate — packaging standard for research data. Common Provenance Model RO-Crate confirmed live (Session G).
- [Workflow Run RO-Crate (PLoS ONE 2024)](https://doi.org/10.1371/journal.pone.0309210) - RO-Crate profile for recording workflow execution provenance. Key for Gap 2.
- [WorkflowHub Registry](https://workflowhub.eu) - FAIR workflow registry using RO-Crate.

## Reproducibility

- [LLM Reproducibility Study (ICSE 2026)](https://arxiv.org/abs/2510.25506) - Empirical LLM reproducibility study for ICSE 2026.
- [R-LAM: Reproducibility-Constrained Large Action Models for Scientific Workflow Automation](https://arxiv.org/abs/2601.09749) - Reproducibility-constrained framework for LLM-driven scientific workflows. PyPI: pip install rlam.
- [The Reproducibility Crisis in LLM Research](https://arxiv.org/abs/2512.00651) - Study on reproducibility in LLM research. ICSE 2026.
- [TIB AIssistant: a Platform for AI-Supported Research](https://arxiv.org/abs/2502.14297) - AI-supported research platform from TIB Hannover. ISWC 2025 (Nara, Japan). Uses ORKG for structured scholarly knowledge.

## Supply Chain (AIBOM)

- [AIBoMGen: Generating an AI Bill of Materials](https://arxiv.org/abs/2601.05703) - Tool and methodology for generating AIBOMs.
- [AIBoMGen: Generating an AI Bill of Materials (CAIN 2026)](https://arxiv.org/abs/2601.05703) - Automated signed AIBOM generation with cryptographic hashing, digital signatures, in-toto attestations. CAIN 2026 (Apr 12-13, Rio). Session H update: confirmed venue.
- [CycloneDX v1.7 (ECMA-424) — ML-BOM, Citations, Crypto](https://cyclonedx.org/specification/overview/) - Final 1.x release (Oct 2025). ML-BOM since v1.5. v1.7 adds Citations (provenance of BOM data), patent fields, expanded crypto. 2026: Transparency Exchange Language (superset with….
- [EU AI Act — GPAI Obligations & AIBOM Relevance](https://medium.com/@michael.hannecke/the-model-bill-of-materials-what-ai-act-auditors-will-ask-for-8bf2da012faa) - GPAI obligations effective Aug 2025. High-risk enforcement Aug 2026. Digital Omnibus may push Annex III to Dec 2027. Context for AIBOM regulatory drivers. Session H monitoring.
- [NIST AI RMF 1.0 — AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/ai-standards) - NIST AI Risk Management Framework. Published January 2023. GenAI Profile: AI 600-1 (2024). Cyber AI Profile: IR 8596 (preliminary draft).
- [Operationalising Artificial Intelligence Bills of Materials](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1735919/abstract) - Accepted January 2026.
- [OWASP AIBOM Generator (Hugging Face)](https://genai.owasp.org/resource/owasp-aibom-generator/) - Open-source AIBOM generator for Hugging Face models. Introduced RSAC 2025, contributed to OWASP GenAI Security Project. AIBOM Generation Handbook in development. Session H monitor….
- [OWASP AIBOM Project](https://owaspaibom.org/) - OWASP project for AI Bill of Materials. Includes AIBOM Generator tool.
- [OWASP GenAI Security Project](https://genai.owasp.org/) - Parent project for AIBOM Generator, Top 10 for LLMs, Agentic Application Security. 10 strategic workstreams. RSAC 2026 (Mar 23-26). Session H monitoring update.
- [SPDX 3.0.1 — AI Profile](https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/) - SPDX AI namespace for documenting AI system artifacts: training data, model architecture, energy consumption, personal data usage. ISO/IEC 5962:2021. Session H monitoring update.

## Tools & Libraries

- [pyzotero](https://pypi.org/project/pyzotero/) - Python wrapper for Zotero API v3.
- [ro-crate-py](https://pypi.org/project/rocrate/) - Python library for creating/manipulating RO-Crates.
- [rocrate-zenodo](https://pypi.org/project/rocrate-zenodo/) - Python tool for depositing RO-Crates to Zenodo.
