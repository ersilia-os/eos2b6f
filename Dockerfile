FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install pandas==2.0.3
RUN pip install rdkit==2024.3.5
RUN pip install svgutils==0.3.4
RUN pip install torch==2.4.1
RUN pip install torch_geometric==2.0.1
RUN pip install torch_sparse==0.6.18
RUN pip install torch_scatter==2.1.2


WORKDIR /repo
COPY . /repo
