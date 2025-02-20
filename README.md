# Tasks
### even_values.py:  
Реализованы две функции определения четности целого числа: делением с остатком на 2 и с помощью побитовой операции.  
Оба варианта очень простые, быстрые. Разница в производительности может быть незначительна и зависит от контекста.

### queues.py:
Реализован циклический буфер с использованием списка и с использованием deque модуля collections. А также проведено сравнение времени выполнения.  
<ins>Плюсы реализации с использованием списка(CircularBufferList)</ins>:  
* Используется массив фиксированного размера. Это позволяет точно контролировать использование памяти.  
* Простая реализация, с использованием стандартного списка, без подключения дополнительных модулей.  
* Быстрое выполнение операций put и get, так как они просто обновляют индексы.  

<ins>Минусы реализации с использованием списка(CircularBufferList)</ins>:  
* Класс не поддерживает динамическое изменение буфера.  

<ins>Плюсы реализации с использованием collections.deque(CircularBufferDeque)</ins>:  
* Автоматическое управление размером. deque позволяет задавать максимальный размер, при превышении которого старые элементы удаляются сами.  
* Благодаря встроенной структуре, код выглядит более читабельно.  

<ins>Минусы реализации с использованием collections.deque(CircularBufferDeque)</ins>:  
* Необходим импорт модуля collections.  
* Может привести к менее предсказуемому потреблению памяти, чем при использовании списка с фиксированным размером.

По быстродействию разница незначительна, но при большом количестве элементов видим, что класс CircularBufferDeque отрабатывает быстрее.

### sort.py:
Реализован алгоритм timsort, используемый в стандартной библиотеке Python для функции sorted() и метода list.sort() отсортирует предоставленный массив чисел быстрее всего, так как он включает в себя сортировки вставками и слиянием.  
Он оптимизирован для работы с уже почти отсортированными массивами. Использует метод слияния, который эффективен для объединения уже отсортированных подмассивов. А для небольших подмассивов использует сортировку вставками, которая эффективна для малых объемов данных.
