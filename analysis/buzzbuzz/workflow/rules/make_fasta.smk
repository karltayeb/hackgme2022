
gtf_path = '/scratch/midway2/ktayeb/anopheles_gambiae/subset.gtf'
genome_path = '/scratch/midway2/ktayeb/anopheles_gambiae/whole_genome.fasta'

prefix = '/scratch/midway2/ktayeb/hackathon/results'

rule gtf2bed:
    input: gtf_path
    output: f'{prefix}/example.bed'
    shell:
        "gtf2bed < {input} > {output}"

rule index_fasta:
    input: genome_path,
    output: genome_path + '.fai'
    shell:
        """
        ml samtools
        samtools faidx {input} > {output}
        """
rule subset_genome:
    input: 
        genome = genome_path,
        idx = genome_path + '.fai',
        bed = f'{prefix}/example.bed'
    output:
        f'{prefix}/subset.fasta'
    shell:
        """
        ml bedtools
        bedtools getfasta -fi {input.genome} -bed {input.bed} > {output}
        """