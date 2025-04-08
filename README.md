**Условие Задачи**

На вход подается список из чисел nums. Изначальное позиционирование на первом элементе списка (nums[0]). Каждый элемент списка представляет собой максимальную длину прыжка с этой позиции. Определите возможно ли добраться до последнего элемента списка. Функция должна вернуть true или false.

Ввод: [2,3,1,1,4]  
Вывод: true  
Из nums[0] можно перепрыгнуть в nums[1] и оттуда в nums[4], что является концом списка.

Ввод: [3,2,1,0,4]  
Вывод: false  
При любом из обстоятельств мы не сможем продвинуться дальше nums[3]

---
**Примеры ввода-вывода**

is_last_element_reachable([2, 3, 1, 1, 4])  
True  
is_last_element_reachable([1, 1, 2, 0, 3, 0, 0, 1])  
True  
is_last_element_reachable([2, 0, 2, 0, 10, 0, 0, 0])  
True  
is_last_element_reachable([3, 2, 1, 0, 4])  
False  
is_last_element_reachable([1, 1, 2, 0, 2, 0, 0, 1])  
False  
is_last_element_reachable([0, 1, 2, 0, 3, 0, 0, 1])  
False  
is_last_element_reachable([1])  
True  
is_last_element_reachable([])  
False  
