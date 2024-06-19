configfile: "config.yaml"

rule all:
    input:
        expand("output/{sample}_Final_processed_igblast_file.tsv", sample=config["samples"]),

rule input_fastq:
    input:
        fastq="samples/{sample}.fastq"
    output:
        with_5g="output/{sample}_first25bps_5g.txt",
        with_4g="output/{sample}_first25bps_4g.txt"
    shell:
        """
        python3 script1.py {input.fastq} {output.with_5g} {output.with_4g}
        """

rule extract_12bpUMI_before5Gs:
    input:
        text_file_5g="output/{sample}_first25bps_5g.txt",
        text_file_4g="output/{sample}_first25bps_4g.txt"
    output:
        Extracted_5g="output/{sample}_Extracted5g.txt",
        Extracted_4g="output/{sample}_Extracted4g.txt"
    shell:
        """
        python3 script2.py {input.text_file_5g} {input.text_file_4g} {output.Extracted_5g} {output.Extracted_4g}
        """
rule separate_repeating_and_nonrepeating_UMIs:
    input:
        extracted_file_5g="output/{sample}_Extracted5g.txt",
        extracted_file_4g="output/{sample}_Extracted4g.txt"
    output:
        output_file1_5g="output/{sample}_repeating_5g.txt",
        output_file2_4g="output/{sample}_repeating_4g.txt"
    shell:
        """
        python3 script3.py {input.extracted_file_5g} {input.extracted_file_4g} {output.output_file1_5g} {output.output_file2_4g}
        """
rule seprate_string_threshold_50:
    input:
        repating_file_5g="output/{sample}_repeating_5g.txt",
        repating_file_4g="output/{sample}_repeating_4g.txt"
    output:
        multi_string_5g="output/{sample}_multiplestrings_5g.txt",
        multi_string_4g="output/{sample}_multiplestrings_4g.txt"
    shell:
        """
        python3 script4.py {input.repating_file_5g} {input.repating_file_4g} {output.multi_string_5g} {output.multi_string_4g}
        """
rule make_4g_unique:
    input:
        multi_file_5g="output/{sample}_multiplestrings_5g.txt",
        multi_file_4g="output/{sample}_multiplestrings_4g.txt"
    output:
        unique_string_4g="output/{sample}_uniquestrings_4g.txt"
    shell:
        """
        python3 script5.py {input.multi_file_5g} {input.multi_file_4g} {output.unique_string_4g}
        """
rule generate__consensus_for_5g_strings:
    input:
        fastq="samples/{sample}.fastq",
        input_5g="output/{sample}_multiplestrings_5g.txt"
    output:
        output1_5g="output/{sample}_consensus_5g.txt"
    shell:
        """
        python3 script6.py {input.fastq} {input.input_5g} {output.output1_5g}
        """
rule generate__consensus_for_4g_strings:
    input:
        fastq="samples/{sample}.fastq",
        input_4g="output/{sample}_uniquestrings_4g.txt"
    output:
        output2_4g="output/{sample}_consensus_4g.txt"
    shell:
        """
        python3 script7.py {input.fastq} {input.input_4g} {output.output2_4g}
rule merging_5g_4g_igblast:
    input:
        input1_1="output/{sample}_consensus_5g.txt",
        input2_2=  "output/{sample}_consensus_4g.txt"
    output:
        output1_1="output/{sample}_merged_consensus.txt",
        output1_2="output/{sample}_umis_only.txt"
    shell:
        """
        python3 script8.py {input.input1_1} {input.input2_2} {output.output1_1} {output.output1_2}
        """
rule blast:
    input:
        input_igblast="output/{sample}_merged_consensus.txt"
    output:
        output_igblast="output/{sample}_igblast_output.tsv"
    shell:
        """
        eval "$(conda shell.bash hook)"
        conda activate igblast
        python3 script9.py {input.input_igblast} {output.output_igblast}
        conda deactivate
        """
rule postignlast:
    input:
        input_igblastout="output/{sample}_igblast_output.tsv",
        input_igblast_string="output/{sample}_umis_only.txt"
    output:
        output_temp = "output/{sample}_igblast_out.tsv",
        output_final="output/{sample}_Final_processed_igblast_file.tsv"
    shell:
        """
        python3 script10.py {input.input_igblastout} {input.input_igblast_string} {output.output_temp} {output.output_final}
        """
