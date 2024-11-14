# SNOWFLAKE_LLMOps
Getting Started with LLMOps using Snowflake Cortex and TruLens

**Overview**
Cortex LLM Functions and Cortex Search, and then using TruLens to add observability and guardrails.

Along the way, you will also learn how run TruLens feedback functions with Snowflake Cortex as the feedback provider, and how to log TruLens traces and evaluation metrics to a Snowflake table. Last, we'll show how to use TruLens guardrails for filtering retrieved context and reducing hallucination.

Here is a summary of what you will be able to learn in each step by following this quickstart:

-   Setup Environment: Create a session to use Snowflake Cortex capabilities.
-   Cortex Complete: Use Cortex Complete() to call Mistral Large.
-   Add Data: Load and preprocess raw documentation from GitHub, and load to Cortex Search.
-   Search: Search over the data loaded to Cortex Search.
-   Create a RAG: Create a RAG with Cortex Search and Complete and add TruLens instrumentation.
-   Feedback Functions: Add context relevance, groundedness and answer relevance evaluations to the RAG.
-   Application Testing: Understand the performance of your RAG across a test set.
-   Guardrails: Add context filter guardrails to reduce hallucinations.
-   Measure Improvement: See the improved evaluation results after adding guardrails.
-   What are Cortex LLM Functions?
-   Snowflake Cortex gives you instant access to industry-leading large language models (LLMs) trained by researchers at companies like Mistral, Reka, Meta, and Google, including Snowflake Arctic, an open enterprise-grade model developed by Snowflake.

**What is Cortex Search?**
Cortex Search enables low-latency, high-quality search over your Snowflake data. Cortex Search powers a broad array of search experiences for Snowflake users including Retrieval Augmented Generation (RAG) applications leveraging Large Language Models (LLMs).

**What is TruLens?**
TruLens is a library for tracking and evaluating Generative AI applications. It provides an extensive set of feedback functions to systematically measure the quality of your LLM based applications. It also traces the internal steps of your application, and allows you to run feedback functions on any internal step. Feedback function results can be examined in a TruLens dashboard, or used at runtime as guardrails.

**What You Will Learn**
- How to build a RAG with Cortex Search and Cortex LLM Functions.
- How to use TruLens Feedback Functions and Tracing.
- How to log TruLens Evaluation Results and Traces to Snowflake.
- How to use TruLens Feedback Functions as Guardrails to reduce hallucination.
  
**What You Will Build**
- A retrieval-augmented generation (RAG) app
- An LLMOps pipeline
- Context filter guardrails
- Prerequisites
- A Snowflake account with Cortex LLM Functions and Cortex Search enabled. If you do not have a Snowflake account, you can register for a free trial account.
- A Snowflake account login with ACCOUNTADMIN role. If you have this role in your environment, you may choose to use it. If not, you will need to 1) Register for a free trial, 2) Use a different role that has the ability to create database, schema, tables, stages, tasks, user-defined functions, and stored procedures OR 3) Use an existing database and schema in which you are able to create the mentioned objects.
