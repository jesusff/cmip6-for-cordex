CMIP6 study collection
======================

This is a collection of results from different studies involving CMIP6 data
(CMIP and ScenarioMIP  activities, historical and SSP-forced experiments). The
information collected supports the selection of GCMs for dynamical downscaling
within CORDEX. In particular, this initiative has been started within the
EURO-CORDEX task force on GCM selection. The information for each CMIP6
ensemble member is collected in [YAML](https://en.wikipedia.org/wiki/YAML)
files in this directory.

The main aim of this collection of information is to have input for
decision-making in the selection of GCMs. The aim for this information is to
be:

 * based on published scientific literature
 * extended by author contributions
 * described by more than just numbers, incorporating decision thresholds
 * traceable, recording the decision process and alternative decisions
 * human readable
 * machine readable

File granularity
----------------

The granularity of the YAML files is irrelevant, since all entries from all
files are concatenated and processed together.

Currently, files are named according to a 3-letter acronym of the first author
and year of publication, but this information is not used while processing the
files. All relevant metrics from a single publication are gathered in a single
file. Any other arrangement to ease the human readability of the files (e.g.
each entry in a separate file, or collect all entries from a given type in a
single file) is also possible.

File structure
--------------

Files are composed of a (YAML) list of entries. Each entry contains all the
information to be processed. That is, it does not depend on other definitions
as in a relational database.

Pros:

 * Entries can be concatenated or split into different files at will.
 * Human readability. Each entry contains all the information. No need to refer
   anywhere else to understand the contents of the entry.

Cons:

 * Longer entries, repeating part of the information

This con can be partly alleviated by using YAML anchors and references (see an
example in the [AtlasIPCC.yaml](AtlasIPCC.yaml) file, with references to the metric and period
defined in the first entry). This simplifies hand writing and manually updating
the entries, partly missing the readability.

An example of the structure of the files can be seen e.g. in
[Oud20.yaml](Oud20.yaml) (for the ` performance` and `future_spread` types) or
in [Bru20.yaml](Bru20.yaml) (for the `independence` type). Note that the syntax
of the YAML files is based on **white space and indentation** and there is no
need for quotes around strings. This highly improves readability, but requires
careful typing. The purpose of the entry keys is described next:

key | subkey | value
---:|--------|:------
key | | This is a unique key, that will appear as header in the summary table when the entries are processed (see e.g. [../CMIP6_perfspread.csv](../CMIP6_perfspread.csv))
doi | | DOI for the reference where the metric was published. No other bibliographic information should be needed. Title, authors, etc. can be automatically retrieved out of the DOI.
type| | Type of metric. Currently choose one of `performance` (performance metric, evaluating historical simulations against observations/reanalysis), `future_spread` (future delta change w.r.t. a reference period) or `independence` (model classification according to their a-priori or output dependence)
metric | | Contains the details of the metric that is coded in this entry
. | name       | a unique name (no spaces)
. | long_name  | a more descriptive name (e.g. to be used as label for a plot axis)
. | units      | units following udunits conventions. The special names `rank` and `binary` are also allowed to indicate a ranking of models or a binary decision metric. Also, `categorical` can be used to indicate that the values are category names. This is usual for `independence` entries. It could be applied to other entries, but it is always preferred to code the metric as a numeric value and code the categories using the `classes` key (see below).
. | variables | variables involved in the metric. CF acronyms in a list. E.g. `[psl, tas]`
. | comment | A more detailed description of the metric, including is location in the reference publication (e.g. Figure or Table number), potential shortcomings, or any other detail not provided in the fields below.
. | best (opt) | This and the next key determine the direction of the metric. Indicate here the best attainable value.
. | worst (opt)| Worst value. `+inf` and `-inf` are allowed
disabled | | This key disables the processing of the entry. Use the sub-keys to specify the cause. See e.g. [Tok20.yaml](Tok20.yaml).
. | cause | Choose one of `preferred_source`, `not_forcing_rcm`
. | preferred | Specify the key(s) of the preferred source(s) for this metric.
. | comment | Brief, free-text explanation for disabling this entry. 
spatial_scope | | Spatial scope of the metric. Area where it applies (Global, a CORDEX domain acronym, an IPCC region, a country name or other region considered in the study)
temporal_scope || Season when the metric applies. Enter `Annual` or a month sequence (`DJF`, `JJA`, ...)
period || Periods relevant for the metric
. | reference | For performance entries, the evaluation period. For future spread, the reference period used in the deltas.
. | target | Target period to compute delta changes.
plausible_values (opt) | | Range of plausible values for the metric.
. | min |
. | max |
. | source | Source of the values. Use one of `reference` (if provided in the text of the peer reviewed reference), `author` (if provided by the authors by personal communication), `eurocordex_gcm_selection_team` if selected after decision of this team.
. | comment (opt) | Recommended if the source is not `reference`, to elaborate on the selection of this range.
classes (opt) || Classification of the metric values into an arbitrary number of categories.
. | limits | list of class limits (in square brackets, comma-separated)
. | labels | labels for each class (in square brackets, comma-separated, one item less than limits)
. | source | See potential values in the `plausible_values` source section.
. | comment (opt) |
data_source | | Source of the actual data provided next. One of `reference` (if the numbers are readily available in the text of the peer reviewed reference), `reference_extracted_from_plot` (if extracted from a plot in the reference), `author` (if provided by the authors by personal communication), `author_extended_model_set` (if the authors provided values for model members beyond those published, but otherwise according to the reference) or `author_adapted` (if the authors provided values adapted in some form, e.g. the reference provides a global analysis and the author repeated the analysis for Europe, or for other season).
data | | Data section providing the metric values. For `future_spread` entries, this data section is arranged using the scenario as sub-key.

Different sets of `plausible_values` and `classes` from different sources can be accomodated in a list.

Pending issues
--------------

 * ~~Coding of multi-member metrics (e.g. data for ensemble means).~~
   - ~~The problem is mainly the input format. Display format can be easily accomodated using an asterisk or similar.~~
   - Member ranges are now supported (see an example in [Tok20.yaml](Tok20.yaml)) and expanded automatically when rendering the table.
 * Hard and soft limits.
   1. Currently, alternative `plausible_values` can be provided. These could be used to define different limits.
   2. Another posibility is to leave the `plausible_values` for the hard limit, and use the `classes` to define a more fine-grained classification (e.g. having extreme `unplausible` levels in the labels).
   3. Yet another posibility is to have `plausible_values` coded as:
   
     ```
     plausible_values:
       hard: [-4, 4]
       soft: [-2, 2]
     ```

   The advantage of 1.+2. is that one can easily highlight separately both
   classifications, as it is done currently with the font color (grey/black) and
   cell background colors.
