# Goodreads Change Log

## [1.8.3] - 2025-04-18
### Fixed
- Fix Get ASIN option so turning it off will no longer retrieve the Amazon identifier.

## [1.8.2] - 2024-06-13
### Fixed
- Fix casing of goodreads identifier in code so right-click remove in calibre feature will work (Terisa).

## [1.8.1] - 2023-03-24
### Fixed
- Author metadata change of just taking the primary contributor (first) when a book has no contributors with a role of Author like comics.

## [1.8.0] - 2023-03-19
### Fixed
- Changed the source from where the authors metadata is being scraped from, to better respect turning off the `Get all contributing authors` setting so as to not always return all authors. Note pseudonyms for authors will return both names. -([#53][i53])

[i53]: https://github.com/kiwidude68/calibre_plugins/issues/53

## [1.7.10] - 2023-03-17
### Added
- Tamil translation

## [1.7.9] - 2023-05-26
### Added
- Latvian translation (@ciepina)
### Fixed
- Publication date not always present in work part of json, so fallback to that in book details json.

## [1.7.8] - 2023-04-22
### Changed
- Large print editions will be ignored if a non large print match is found first.

## [1.7.7] - 2023-04-14
### Fixed
- Support calibre versions 5.9.0 to 5.39.1 which did not have a random chrome user agent function.

## [1.7.6] - 2023-04-05
### Fixed
- Add retry logic for situations where Goodreads is returning invalid html responses (max 10 attempts).

## [1.7.5] - 2023-04-04
### Changed
- **Breaking:** Require calibre 2.81.0 or later due to change in 1.7.4 for random chrome user agent. Use calibre 6.x for a better guarantee it will work.
- Parsing authors now includes all with same contributing type as first author in list (only applies when Get all contributing authors is unchecked).

## [1.7.4] - 2023-04-02
### Changed
- Dutch translation (@M. de Boer)
### Fixed
- Fix to handle Goodreads working best only with Chrome based browsers. (@changhuapeng)

## [1.7.3] - 2023-02-01
### Fixed
- Fix to handle books with no contributors. (@busches)
- Fix for legacy comments parsing with no strip() function. (@MartinCa)

## [1.7.2] - 2022-12-24
### Fixed
- Return None rather than empty string when no description present, for better result merging.

## [1.7.1] - 2022-10-16
### Added
- German translation (@Dustin Steiner)
- Portuguese translation (@Comfy.n)
- Added an option to ignore all genre -> tag mappings, to get all genres from Goodreads. Increase your `Max number of tags to download` setting if you use this option because you may miss tags otherwise.
### Changed
- No longer support hierarchical genres (as not in new website design). So a book with genres of `Fantasy` and `Fantasy > Urban Fantasy` will get returned with `Fantasy` and `Urban Fantasy` genres instead on old web pages. The new web page design will also return the same. Users should review their genre mappings in the configuration dialog and replace any `X > Y` hierarchical mappings with one for just `Y` instead.

## [1.7.0] - 2022-09-24
_All kiwidude plugins updated/migrated to: https://github.com/kiwidude68/calibre_plugins_
### Added
- Added configuration option to download precise Goodreads rating and review vote count into two identifiers `grrating` and `grvotes`
    - The new identifiers can be bound to custom columns in calibre.
    - See `README.md` for details of how to do this.
- Added Russian translations (@Caarmi)
### Changed
- **Breaking:** Drop PyQt4 support, require calibre 2.x or later.
- Refactoring of common code

## [1.6.2] - 2022-09-08
### Added
- Add translation support for config screen.
- Chinese, Spanish, French, Hungarian, Italian, Japanese, Dutch, Polish, Ukranian translations - thanks to everyone!!!

## [1.6.1] - 2022-09-06
### Added
- Add configuration option to use edition published date or first published date (default).
### Fixed
- Remove debug code, fixes for isbn, publication date and series index when multiple series.

## [1.6.0] - 2022-09-03
### Changed
- Support new Goodreads web page formats in conjunction with legacy pages.

## [1.5.3] - 2022-01-05
### Changed
- Cleanup in preparation for calibre 6/Qt6. (@davidfor)

## [1.5.2] - 2020-11-30
### Fixed
- Use mobi-asin identifier  (@davidfor)

## [1.5.1] - 2020-09-25
### Added
- Czech translation (@seeder)
- Add download page count from databazeknih.cz and cbdb.cz (@seeder)
### Fixed
- Wasn't getting the series info.

## [1.5.0] - 2020-09-19
### Changed
- Changes for Python 3 support in calibre. (@davidfor)
### Fixed
- Small error in handling editions.

## [1.4.0] - 2018-12-20
### Fixed
- Site change for rating. (@davidfor)
- Add extra attempt to convert language name to code.

## [1.3.0] - 2018-11-10
### Added
- Add get_book_url for pasting URL and getting an identifier. (@davidfor)
### Changed
- Generate HTTPS URL for identifier.

## [1.2.0] - 2018-10-23
### Added
- Add search by ASIN or other Amazon id if it exists. (@davidfor)
- Use auto_complete API for ISBN and ASIN search. Based on code from MR user botmtl. 

## [1.1.17] - 2018-10-13
### Fixed
- Changes in search page plus fixing issue with scanning editions. (@davidfor)

## [1.1.16] - 2018-10-03
### Added
- Get the ASIN if the book is am Amazon edition. There is an option to turn this on. It is off by default. (@davidfor, @Iceybones)
### Changed
- Checks through the search results for a match to the title and author.
### Fixed
- Series separated from the title.

## [1.1.14] - 2018-04-17
### Fixed
- Change in search page. (@davidfor)

## [1.1.13] - 2017-12-17
### Fixed
- Normalize title to solve issues with accented characters. (@davidfor)

## [1.1.12] - 2016-12-30
### Fixed
- Ratings were not always being retrieved properly. (@davidfor)

## [1.1.11] - 2016-02-08
### Fixed
- Site changes for the description/comments. (@davidfor)
- Site and option changes for genre and classification. 

## [1.1.10] - 2015-10-26
### Fixed
- Site changes for the description/comments.

## [1.1.9] - 2015-07-11
### Fixed
- Do not change case of tags downloaded, so YA stays as YA.

## [1.1.8] - 2014-07-08
### Changed
- Change to allow Qt4 or Qt5.

## [1.1.7] - 2013-08-25
### Fixed
- For more.../less... on authors

## [1.1.6] - 2013-08-17
### Added
- Support Dutch language

## [1.1.5] - 2013-07-10
### Fixed
- Updated to match Goodreads website change which broke ISBB and cover parsing

## [1.1.4] - 2013-03-04
### Fixed
- Goodreads change for when large number of authors to ensure more.../less... is removed correctly

## [1.1.3] - 2012-12-28
### Added
- Support for "languages" metadata field
### Fixed
- Get all contributing authors option

## [1.1.2] - 2012-06-23
### Fixed
- Reject editions that do not match in title (such as different languages) and handle non-ascii characters better
- Handle books with short descriptions since Goodreads website change

## [1.1.1] - 2012-06-12
### Fixed
- Match Goodreads website change which stopped tags being downloaded
- Change to the comments to no longer strip paragraph breaks

## [1.1.0] - 2012-0303
### Fixed
- The "Scan multiple editions for title/author searches" option broken from Goodreads website change

## [1.0.9] - 2011-11-14
### Added
- Support case insensitive comparisons of genre tag mappings
- Allow renaming an item changing only case
### Changed
- When sorting to display the mappings in the config screen, ignore case

## [1.0.8] - 2011-10-25
### Fixed
- If large number of authors, ensure more... and ...less is stripped from authors results.

## [1.0.7] - 2011-08-10
### Fixed
- Ensure a "close but not quite" series # does not throw an error within the plugin.

## [1.0.6] - 2011-06-21
### Fixed
- Handle change to Goodreads website which prevented title/author results returning

## [1.0.5] - 2011-05-12
### Changed
- Ensure any covers less than 1000 bytes in size are ignored.
- No longer prefix the comments with SUMMARY: in output for consistency with other plugins

## [1.0.4] - 2011-05-08
### Changed
- Remove code supporting versions prior to 0.8
- Strip trailing comma from series name if it exists
- Put summary comments on line following the word SUMMARY: rather than on same line.

## [1.0.3] - 2011-04-29
### Fixed
- Ensure non ascii author names are parsed correctly.

## [1.0.2] - 2011-04-26
### Fixed
- Properly fix the ordering of tags.

## [1.0.1] - 2011-04-25
### Changed
- Support for API change upcoming in Calibre 0.7.58 allowing hyperlinked ids in book details panel
### Fixed
- Ensure tags mapped are returned by order of popularity not alphabetically so applying a tag threshold works better

## [1.0.0] - 2011-04-23
_Initial release of plugin, rewritten consolidation of Goodreads Metadata and Goodreads Covers plugins_
