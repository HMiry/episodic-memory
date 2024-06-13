# Ego4D Natural Language Queries (NLQ) Challenge

Welcome to our repository for the Ego4D NLQ Challenge. Here, we are advancing video understanding by integrating cutting-edge video-language models to address natural language queries using egocentric video data.

## Project Overview

Our team leverages the extensive Ego4D egocentric video dataset to address the Natural Language Queries (NLQ) benchmark. This benchmark challenges models to identify video segments that answer specific natural language queries, enhancing the interaction between visual content and human language.

### Key Steps and Modifications

1. **Model Training**: We trained multiple configurations of the VSLBase and VSLNet models, specifically:
   - `VSLNet_with_omnivore`
   - `VSLNet_with_egovlp`
   - `VSLNet_glove`
   - `VSLBase_with_omnivore`
   - `VSLBase_with_egovlp`
   
   These models were trained on pre-extracted features from EgoVLP and Omnivore, showcasing improvements over traditional models using SlowFast features.
   
2. **Feature Handling**: Integration of advanced features demonstrates superior handling of egocentric video data.
3. **Custom Encoder Implementation**: We transitioned from BERT to GloVe for text encoding to analyse the linguistic comprehension.
4. **Query Answering Extension**: Utilizing the Video-LLaVA model, we generated textual responses from video segments accurately retrieved by VSLNet for selected NLQ queries.

### Extension and Innovation

Our innovative workflow generates direct textual answers from video segments:
1. **Query Selection**: We chose 50 precise queries where VSLNet accurately retrieved the correct video segments.
2. **Segment Extraction**: Using ffmpeg, we extracted the relevant video segments.
3. **Textual Answer Generation**: Employed the Video-LLaVA model to produce textual answers from the video data.

## Repository Content

- **NoteBooks**: This newly added folder contains detailed Jupyter notebooks documenting our experiments and their results. Each notebook corresponds to a specific model configuration or part of our pipeline:
  - `VSLNet_with_omnivore.ipynb`
  - `VSLNet_with_egovlp.ipynb`
  - `VSLNet_glove.ipynb`
  - `VSLBase_with_omnivore.ipynb`
  - `VSLBase_with_egovlp.ipynb`
  - `VideoLLava.ipynb` – Details the creation of `sampled_nlq_data.json` from `nlq_val.json` and `vslnet_19_6460_preds.json`, which are also stored within the `jsons` sub-folder.

### Detailed Steps

#### Data and Setup
- **Environment Setup**: Instructions for setting up the environment and installing necessary tools.
- **Data Integrity Check**: Verify the integrity of the downloaded files to ensure data consistency.

#### Model Training and Evaluation
- **Training Models**: Steps to train each configuration using pre-extracted features.
- **Performance Evaluation**: Compare the results with baseline models to highlight improvements.

#### Extension - Query Answer Generation
- **Video Segment Extraction**: Methods for extracting video segments corresponding to selected queries.
- **Textual Answer Generation**: Using the Video-LLaVA model to generate textual responses directly from the video segments.

## Results

Our results demonstrate significant improvements over baseline models, providing robust capabilities in generating direct textual responses, thus enhancing the practical usability of video query systems.

## Challenges and Further Information
- [NLQ Challenge Overview](https://eval.ai/web/challenges/challenge-page/1629/overview)
- [Discussion on NLQ Annotation Issues](https://discuss.ego4d-data.org/t/nlq-annotation-zero-temporal-windows/36)

## License

This project is released under the MIT License. Details are provided in the LICENSE file.

## More Information

For more detailed documentation and setup instructions, or to download the dataset, please visit [Ego4D Documentation](https://ego4d-data.org/docs/).

This README is structured to clearly convey the scope, methodology, and outputs of your project, ensuring that collaborators and researchers can easily understand and engage with your work.