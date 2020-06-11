#Download Tensorflow models & tools
cd {BASE_DIR}
mkdir temp
cd temp
git clone https://github.com/tensorflow/models.git && (cd models && git checkout f788046ca876a8820e05b0b48c1fc2e16b0955bc)
mv models {BASE_DIR}
cd {BASE_DIR}
rmdir {BASE_DIR}/temp
