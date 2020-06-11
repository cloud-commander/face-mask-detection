#Download Tensorflow models & tools
cd /content/tensorflow
mkdir temp
cd temp
git clone https://github.com/tensorflow/models.git && (cd models && git checkout f788046ca876a8820e05b0b48c1fc2e16b0955bc)
mv models /content/tensorflow
cd /content/tensorflow
rmdir /content/tensorflow/temp
