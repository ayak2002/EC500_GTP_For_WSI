export CUDA_VISIBLE_DEVICES=0
python main.py \
--n_class 6 \
--data_path "./graphs" \
--val_set "./graphs/test_set.txt" \
--model_path "./graph_transformer/saved_models/" \
--log_path "./graph_transformer/runs/" \
--task_name "GTP" \
--batch_size 1 \
--test \
--log_interval_local 6 \
--resume "./graph_transformer/saved_models/GTP.pth"
