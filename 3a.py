# а) Дан текст, за яким слідує крапка. В алфавітному порядку вивести на екран (по разу)
# усі малі українські голосні букви, що входять в цей текст.

letters = set('аеиіоу')
while True:
    text = set(input().replace(' ', ''))
    text.discard('.')
    for i in sorted(list(text.intersection(letters))):
        print(i)
    if not input('One more? (YES - Enter, NO - something)'):
        continue
    break
