FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install pandas
RUN pip install rdkit-pypi==2022.3.1b1
RUN pip install svgutils
RUN pip install torch
RUN pip install torch_geometric==2.0.1
RUN pip install torch_sparse
RUN pip install torch_scatter
RUN conda install -c conda-forge xorg-libxrender xorg-libxtst

WORKDIR /repo
COPY . /repo
