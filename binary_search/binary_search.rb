def binary_search(input, value)
  if input.empty?
    return false
  end
  mid = input.length / 2
  if input.length == 1
    return value == input[0]
  end
  if input[mid] == value
    return true
  elsif value < input[mid]
    return binary_search(input.slice(0, mid), value)
  elsif value > input[mid]
    return binary_search(input.slice(mid, input.length), value)
  end
  return false
end

r = Random.new
input = Array.new(500){|n| r.rand(1000)}
input = input.sort
puts binary_search(input, 100)
puts binary_search(input, 1000)
puts binary_search(input, 500)

