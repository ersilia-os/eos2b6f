FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install pandas=1.3.5
RUN pip install rdkit-pypi==2022.3.1b1
RUN pip install svgutils==0.3.4
RUN pip install torch==1.13.1
RUN pip install torch_geometric==2.0.1
RUN pip install torch_sparse==0.6.17
RUN pip install torch_scatter==2.1.1
RUN conda install -c conda-forge xorg-libxrender xorg-libxtst

WORKDIR /repo
COPY . /repo
