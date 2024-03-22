export CUDA_VISIBLE_DEVICES=0
python main.py \
--n_class 6 \
--data_path "./graphs" \
--train_set "./graphs/train_set.txt" \
--val_set "./graphs/val_set.txt" \
--model_path "./graph_transformer/saved_models/" \
--log_path "./graph_transformer/runs/" \
--task_name "GTP" \
--batch_size 2 \
--train \
--log_interval_local 6 \
