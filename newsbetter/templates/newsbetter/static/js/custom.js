/* global compileExpression */


/*---------------------------------------------------------------------------*/
/*  DataTables
/*---------------------------------------------------------------------------*/

// // Enable DataTables to sort based on type (e.g. dates)
// $.fn.dataTable.moment = (format, locale) => {
//   const types = $.fn.dataTable.ext.type;
//
//   // Add type detection
//   types.detect.unshift((d) => {
//     const valid = moment(d, format, locale, true).isValid();
//     if (valid) {
//       return `moment-${format}`;
//     }
//     return null;
//   });
//
//   // Add sorting method: use integer
//   types.order[`moment-${format}-pre`] = d => (
//     moment(d, format, locale, true).unix());
// };

// Search for articles based on article search box
$.fn.dataTable.ext.search.push(
  (settings, data) => {
    const title = data[1]; // eslint-disable-line no-unused-vars
    const searchString = $('#article_search').val();

    function titleIncludes(s) {
      return title.toLowerCase().includes(s.toLowerCase()) ? 1 : 0;
    }

    // Let's try and parse the search string
    let articleSearch;
    try {
      articleSearch = compileExpression(searchString, { t: titleIncludes });
      // The search string was valid, so let's return the result
      return articleSearch() === 1;
    } catch (err) {
      // We couldn't parse the string
      // If the search field is blank, show all rows, otherwise none
      return searchString.length === 0;
    }
  },
);

/*---------------------------------------------------------------------------*/
/*  After document has loaded
/*---------------------------------------------------------------------------*/

$(document).ready(() => {
  // Allow table sorting of specific date format
  $.fn.dataTable.moment('DD MMM YYYY');

  // Create DataTable for article list
  const articleList = $('#article_list').DataTable({
    pageLength: 50,
  });
  // (() => new $.fn.dataTable.ColReorder(articleList))();

  // Update article list whenever we change the article search field
  $('#article_search').keyup(() => {
    articleList.draw();
  });
});
