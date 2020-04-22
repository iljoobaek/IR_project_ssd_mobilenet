python eval_ssd.py --dataset_type voc \
        --dataset /home/karan/data/VOCdevkit2007/VOC2007 \
        --net mb2-ssd-lite \
        --trained_model models/ssd_mobilenet2/mb2-ssd-lite-Epoch-0-Loss-1.0990761518478394.pth \
	--label_file models/voc-model-labels.txt
