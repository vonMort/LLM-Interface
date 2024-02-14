from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset
from src.logger import print_like_human


def trainer_logic():
    print_like_human('Loading the IMDB dataset...')
    dataset = load_dataset('imdb')

    print_like_human('Loading the tokenizer...')
    tokenizer = AutoTokenizer.from_pretrained('')  #TODO find correct tokenizer
    print_like_human('Loading successful.')

    def tokenize_function(examples):
        return tokenizer(examples['text'], padding='max_length', truncation=True)

    tokenized_datasets = dataset.map(tokenize_function, batched=True)

    train_dataset = tokenized_datasets['train']
    test_dataset = tokenized_datasets['test']

    training_args = TrainingArguments(
        output_dir='.//results',
        evaluation_strategy='epoch',
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=3,
        weight_decay=0.01,
    )
    llm = AutoModelForSequenceClassification.from_pretrained('') #TODO make model path more dynamic
    trainer = Trainer(
        model=llm,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
    )

    print_like_human('Training started...')
    trainer.train()
    llm.save_pretrained('.//model//finetuned_wolfram')
    print_like_human("Model trained and saved at './/model//finetuned_wolfram'")
