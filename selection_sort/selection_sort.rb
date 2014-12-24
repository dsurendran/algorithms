
def selection_sort(input)
  for i in 0..input.length-1
    for j in i..input.length-1
      if input[i] > input[j]
        input[i], input[j] = input[j], input[i]
      end
    end
  end
  return input
end


rand = Random.new
input = Array.new(500) { |num| rand.rand(500) }

p selection_sort(input)