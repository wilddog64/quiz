#!/usr/bin/env perl
use warnings;
use Data::Dumper;
use open ':std', ':encoding(UTF-8)'; # make console handle utf-8 characters

# build our lookup table first by reading all the word from lower-cases.txt
sub buildDict {
    my $filename = shift;
    my $dict = {};

    my $fh;
    open($fh, '<:encoding(UTF-8)', $filename) or die "unable to open $filename\n";
    while (my $line = <$fh>) {
        chomp $line;
        $dict->{$line} = $line;
    }

    return $dict;
}

# here we try to find acrostic word and count how many of them.
# We didn't remove duplicate acrostic words
sub findAcrostic {
    my $filename = shift;
    my $dict     = shift;

    open($fh, '<:encoding(UTF-8)', $filename) or die "unable to open $filename\n";
    my $acrosticFound = 0;
    while( my $line = <$fh> ) {
        chomp $line;
        
        # combine first character of each words from a sentence into a lower cases
        $acrostic = join('', map { lc substr $_, 0, 1 } (split ' ', $line));
        if ( exists $dict->{$acrostic} ) {    # lookup acrostic from our dictionary
           if (length($acrostic) >= 4) {      # only word that's equal to or bigger than 4 characters counts
               $acrosticFound++;              # track down how many acrostic we have found so far
               print "$acrostic --> $line\n"; # print out acrostic and its orignal tweet
           }
        }
    }
    print "Total acrostic words found: $acrosticFound\n"
}

my $dict = buildDict('./words-lowercase.txt'); # building lookup table by reading words-lowercase.txt
# print Dumper $dict;
findAcrostic('./tweets.txt', $dict)
