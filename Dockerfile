FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -f model/framework/pkasolver/devtools/conda-envs/test_env.yaml
# RUN python model/framework/pkasolver/setup.py install

WORKDIR /repo
COPY . /repo
