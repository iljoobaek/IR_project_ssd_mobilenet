python train_ssd.py --dataset_type voc \
        --datasets /home/rtml/data/VOCdevkit2007/VOC2007 \
        --validation_dataset /home/rtml/data/VOCdevkit2007/VOC2007 \
        --net mb1-ssd \
        --base_net models/mobilenet_v1_with_relu_69_5.pth \
        --checkpoint_folder models/ssd_mobileV1 \
        --scheduler cosine \
        --lr 0.001 \
        --batch_size 8 \
        --t_max 200 \
        --validation_epochs 50 \
        --num_epochs 40000 \

