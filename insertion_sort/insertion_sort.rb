def insertion_sort(input)
  for i in 1..input.length-1
    key = input[i]
    j = i - 1
    while j >= 0 and input[j] > key
      input[j+1] = input[j]
      j = j - 1
    end
    input[j+1] = key
  end
  return input
end



rand = Random.new
input = Array.new(500) { |num| rand.rand(500) }

p insertion_sort(input)