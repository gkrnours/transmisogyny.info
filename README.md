# transmisogyny.info
Source for static website transmisogyny.info -- Dedicated to explaining
transmisogyny

## Building the site

transmisogyny.info is a static website built with pelican.

The `content` directory contains all the content of the website in the
form of markdown file with metadata. The files `pelicanconf.py` contains
information about how to put the content together. The folder
`iridescent` hold the theme currently used for the site. The build go to
`output`.

### Using pelican

To put everything together, we use pelican. It is a python program. You
can install it with your system package manager or using pip. `pip
install --user pelican markdown` will install pelican with its markdown
dependency as an user, without needing sudo or root access. The binary
should be in \~/.local/bin/`

Once you have the binary in your path, you can use the included makefile
to generate the static website. If you are using a BSD system, it need
GNU make.

`make help` give you the list of available commands. `make html` will
use pelican to create the site and `make serve PORT=3000` will start a
server serving the content of your `output` directory, listening on
[port 3000](http://localhost:3000). `make html DEBUG=1` will print more
information in case something is not working

### Writing content

Pelican can accept a few different syntax for the content. All have two
part, a section holding the metadata which are information and options
for that piece of content, the section with the actual content.

The metadata in markdown file come at the start of the file and take the
format `Key: value`. If value is a list, like for tags, use comma as
separator. Pelican also try to gather metadata from the files
themselves, like the containing directory for the category and the date
of creation.

Some of these metadata are required, like `title` and `date` for
articles. Other are optional like `tags`. There is no concept
non-existing key, so there will be no error in case of a typo in an
optional key. Be careful.

Add a blank line after the last line of metadata then add the content.
If you have never written markdown, here is a really quick reference.

 * `#Title` starts with one to six # symbol, with one being the most important.
 * Leave a blank line to create a new paragraph.
 * `- list item` starts with a dash or an asterisk followed by a space
 * `1. ordered list item` starts with a number and a dot followed by a space
 * `[link](http://example.org)` has a displayed part and an url part
 * `![image](picture.jpg)` are link starting with a bang. The displayed
   part is the alt-text.
