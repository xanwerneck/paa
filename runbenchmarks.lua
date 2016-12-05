#!/bin/env lua

-- Configuration:
local n_runs = 10
local supress_errors = false
local n_questions = 3
local instances = {
    'instances/Data-120-Q1.txt',
    'instances/Data-120-Q2.txt',
    'instances/Data-120-Q3.txt',
    'instances/Data-120-Q4.txt',
    'instances/Data-250-Q1.txt',
    'instances/Data-250-Q2.txt',
    'instances/Data-250-Q3.txt',
    'instances/Data-250-Q4.txt',
    'instances/Data-500-Q1.txt',
    'instances/Data-500-Q2.txt',
    'instances/Data-500-Q3.txt',
    'instances/Data-500-Q4.txt',
    'instances/Data-1000-Q1.txt',
    'instances/Data-1000-Q2.txt',
    'instances/Data-1000-Q3.txt',
    'instances/Data-1000-Q4.txt',
}

-- Runs the cmd a single time and returns the time elapsed
local function measure(cmd)
    local time_cmd = '{ TIMEFORMAT=\'%3R\'; time ' ..  cmd ..
            ' > /dev/null; } 2>&1'
    local handle = io.popen(time_cmd)
    local result = handle:read("*a")
    local time_elapsed = tonumber(result)
    handle:close()
    if not time_elapsed then
        error('Invalid output for "' .. cmd .. '":\n' .. result)
    end
    return time_elapsed
end

-- Runs the cmd $n_runs and returns the fastest time
local function benchmark(cmd)
    local min = 999
    for _ = 1, n_runs do
        local time = measure(cmd)
        min = math.min(min, time)
    end
    return min
end

-- Measures the time for each instance and question
-- Returns a matrix with the result (instance x question)
local function run_all()
    local results = {}
    for _, instance in ipairs(instances) do
        local rline = {}
        for q = 1, n_questions do
            local cmd = 'python3 knapsack.py ' .. instance .. ' ' .. tostring(q)
            io.write('running "' .. cmd .. '"... ')
            local time = 0
            local ok, msg = pcall(function()
                time = benchmark(cmd)
            end)
            if not ok and not supress_errors then
                io.write('error:\n' .. msg .. '\n---\n')
                os.exit(1)
            end
            table.insert(rline, time)
            io.write('done\n')
        end
        table.insert(results, rline)
    end
    return results 
end

-- Creates and saves the gnuplot data file
local function create_data_file(results, fname)
    local data = 'instance\\question\t'
    for q = 1, n_questions do
        data = data .. tostring(q) .. '\t'
    end
    data = data .. '\n'
    for i, instance in ipairs(instances) do
        data = data .. instance .. '\t'
        for j = 1, n_questions do
            data = data .. results[i][j] .. '\t' 
        end
        data = data .. '\n'
    end
    local f = io.open(fname, 'w')
    f:write(data)
    f:close()
end

local function main()
    local results = run_all()
    create_data_file(results, 'benchmarks.txt')
    print('final done')
end

main()

