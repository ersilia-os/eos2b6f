FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

# RUN conda install -c conda-forge rdkit=2021.03.4
RUN conda install -f model/framework/pkasolver/devtools/conda-envs/test_env.yaml
RUN python model/framework/pkasolver/setup.py install
# RUN pip install joblib==1.1.0

WORKDIR /repo
COPY . /repo
