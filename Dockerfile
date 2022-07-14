FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install pandas
RUN conda install -c conda-forge rdkit=2021.03.4
RUN pip install svgutils
RUN pip install torch
RUN pip install torch_geometric==2.0.1
RUN pip install torch_sparse
RUN pip install torch_scatter

WORKDIR /repo
COPY . /repo
