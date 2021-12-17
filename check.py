if True:
    import transformers

    from transformers import (
        BartTokenizer,
        BartForConditionalGeneration,
    )

    print(f'** transformers v{transformers.__version__} **')

    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large')
    model1 = BartForConditionalGeneration.from_pretrained('facebook/bart-large')
    model1.config.force_bos_token_to_be_generated = True


    input_txt = 'This is <mask> sentence.'
    print(f'Input: "{input_txt}"')

    inputs1 = tokenizer.encode(input_txt, return_tensors='pt')
    outputs1 = model1.generate(inputs1)
    output_txt1 = tokenizer.decode(outputs1[0], skip_special_tokens=True)

    print(f'Output: "{output_txt1}"')



# ############
# if False:
#     from transformers import BartModel
#     from kobart import get_pytorch_kobart_model, get_kobart_tokenizer
#     tokenizer = get_kobart_tokenizer()
#     model = BartModel.from_pretrained(get_pytorch_kobart_model())

#     input_txt = '이것은 <mask> sentence.'
#     print(f'Input: "{input_txt}"')

#     inputs = tokenizer.encode(input_txt, return_tensors='pt')
#     outputs = model.generate(inputs)

#     print(outputs)
#     output_txt = tokenizer.decode(outputs, skip_special_tokens=True)
#     # output_txt = tokenizer.decode(outputs[0], skip_special_tokens=True)

#     print(f'Output: "{output_txt}"')


#     # inputs = kobart_tokenizer(['안녕하세요.'], return_tensors='pt')
#     # model(inputs['input_ids'])


# from transformers import BartModel
# from kobart import get_pytorch_kobart_model, get_kobart_tokenizer
# kobart_tokenizer = get_kobart_tokenizer()
# # model2 = BartModel.from_pretrained(get_pytorch_kobart_model())
# model2 = BartForConditionalGeneration.from_pretrained(get_pytorch_kobart_model())
# inputs2 = kobart_tokenizer(['안녕하세요.'], return_tensors='pt')
# outputs2 = model2(inputs2['input_ids'])
# outputs2 = model2.generate(inputs2['input_ids'])

# output_txt2 = tokenizer.decode(outputs2[0], skip_special_tokens=True)
# dfdf = 0