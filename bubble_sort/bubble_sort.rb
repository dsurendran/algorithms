
def bubble_sort(array)
  for i in 0..array.length
    for j in i..array.length - 1
      if array[i] > array[j]
        array[i], array[j] = array[j], array[i]
      end
    end
  end
  return array
end

rand = Random.new
array = Array.new(100){ |num| rand.rand(500)}

puts bubble_sort(array)