#Download Tensorflow models & tools
mkdir temp && cd temp
git clone https://github.com/tensorflow/models.git && (cd models && git checkout f788046ca876a8820e05b0b48c1fc2e16b0955bc)
cp -r /content/temp/* /content/tensorflow/ && rm -R /content/*
