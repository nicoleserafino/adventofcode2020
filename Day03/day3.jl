using CircularArrays
using Underscores

get_data(filename) = @_ readlines(filename) .|>
    collect .|> (_ .== '#') |>
    hcat(__...) |> CircularArray

part1(data, slope = (3, 1)) = count(1:size(data, 2) ÷ slope[2]) do i
    idx = (1, 1) .+ slope .* i
    data[idx...]
end

@_ get_data("2020/Day03/input.txt") |> part1 |> println("Part 1 answer: ", __)

part2(data) = @_ [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] |>
    part1.(Ref(data), __) |> prod

@_ get_data("2020/Day03/input.txt") |> part2 |> println("Part 2 answer: ", __)