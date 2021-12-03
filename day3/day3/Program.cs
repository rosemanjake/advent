using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.IO;
using System.Diagnostics;
using System.Text.RegularExpressions;
using System.Drawing;

namespace day3
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = getInput("day3.txt");
            List<string> binary = input.Split("\n").ToList();
            binary = cleanUp(binary);

            List<Dictionary<char, int>> counts = getFreqs(binary);
            long gamma = getFinal(counts, "gamma");
            long epsilon = getFinal(counts, "epsilon");   

            Console.Write($"Solution for Part 1 is:\ngamma = {gamma}\nepsilon = {epsilon}");

            List<string> ox = part2(binary, "ox");
            List<string> co = part2(binary, "co");
            Console.Write($"\n\nSolution for Part 2 is:\noxygen generator rating = {ox[0]}\nC02 scrubber rating = {co[0]}");
        }

        static List<string> part2(List<string> binary, string type)
        {
            List<string> retlist = binary;

            for (int i = 0; i < 12; i++)
            {
                retlist = filterList(retlist, type, i);
            }

            return retlist;
        }

        static List<string> filterList(List<string> binary, string type, int index)
        {
            if (binary.Count == 1)
            {
                return binary;
            }

            List<string> filtered = new List<string>();
            List<Dictionary<char, int>> freqs = getFreqs(binary);

            int zerofreq = freqs[index]['0'];
            int onefreq = freqs[index]['1'];

            char target = '0';

            if (type == "ox")
            {
                if (zerofreq > onefreq){
                    target = '0';
                }
                if (zerofreq == onefreq)
                {
                    target = '1';
                }
                if (onefreq > zerofreq)
                {
                    target = '1';
                }
            }        
            else if(type == "co")
            {
                if (zerofreq < onefreq)
                {
                    target = '0';
                }
                if (zerofreq == onefreq)
                {
                    target = '0';
                }
                if (onefreq < zerofreq)
                {
                    target = '1';
                }
            }

            foreach (string num in binary)
            {
                if (num[index] == target)
                {
                    filtered.Add(num);
                } 
            }

            return filtered;
        }

        static long getFinal(List<Dictionary<char, int>> counts, string type)
        {
            string final = "";
            foreach (Dictionary<char, int> digit in counts)
            {
                int zerofreq = digit['0'];
                int onefreq = digit['1'];

                if (type == "gamma")
                {
                    if (zerofreq > onefreq)
                    {
                        final = final + "0";
                    }
                    else
                    {
                        final = final + "1";
                    }
                }
                else if (type == "epsilon")
                {
                    if (zerofreq < onefreq)
                    {
                        final = final + "0";
                    }
                    else
                    {
                        final = final + "1";
                    }
                }
            }

            return long.Parse(final);
        }

        static List<string> cleanUp(List<string> binary)
        {
            List<string> retlist = new List<string>();

            foreach (string num in binary)
            {
                retlist.Add(Regex.Replace(num, @"[ \r]$", ""));
            }

            return retlist;
        }

        static List<Dictionary<char, int>> getFreqs(List<string> binary)
        {
            List<Dictionary<char, int>> final = new List<Dictionary<char, int>>();
            int digitcount = binary[0].Length;

            for (int i = 0; i < digitcount; i++)
            {
                final.Add(getFreq(binary, i));
            }

            return final;
        }

        static Dictionary<char, int> getFreq(List<string> binary, int index)
        {
            Dictionary<char, int> counter = new Dictionary<char, int>();

            foreach (string num in binary)
            {      
                char target = num[index];
                if (!counter.Keys.Contains(target))
                    counter[target] = 0;
                else
                    counter[target]++;
            }

            return counter;
        }

        static string getInput(string target)
        {
            string dir = Directory.GetParent(Directory.GetCurrentDirectory()).Parent.Parent.FullName;
            string[] files = Directory.GetFiles(dir);

            foreach (string file in files)
            {
                if (Path.GetFileName(file) == target)
                {
                    return File.ReadAllText(file);
                }
            }

            return "Target file not found";
        }
    }
}
