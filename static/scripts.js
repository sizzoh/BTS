// $(function() {
//     function expenseChart(){
//         const chart = document.getElementById("expenseChart").getContext("2d");
//         $(document).ready(function(){
//           $.ajax({
//             type: "GET",
//             url: "/expenseAccounts",
//             dataType: "json",
//             csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
//             success: function(data){
      
//               var expense = data.ex_data;
//               var expenseTotal = data.ex_data3;
      
//               //get expense for each day
//                       var monday_expense_amount = expense[7];
//                       var tuesday_expense_amount = expense[8];
//                       var wednesday_expense_amount = expense[9];
//                       var thursday_expense_amount = expense[10];
//                       var friday_expense_amount = expense[11];
//                       var saturday_expense_amount = expense[12];
//                       var sunday_expense_amount = expense[13];
      
             
//                        //get days to set its text budget amounts
//                       var monday_amount = $("#monday_amount_expense");
//                       var tuesday_amount = $("#tuesday_amount_expense");
//                       var wednesday_amount = $("#wednesday_amount_expense");
//                       var thursday_amount = $("#thursday_amount_expense");
//                       var friday_amount = $("#friday_amount_expense");
//                       var saturday_amount = $("#saturday_amount_expense");
//                       var sunday_amount = $("#sunday_amount_expense");
//                       var weekly = $("#weeklyExpense");
//                       var weekly_amount = $("#weekly_amount_expense");
                      
//                       //create graph for each expense day
//                       let chartBrowser = new Chart(chart, {
//                         type: "bar",
//                         data: {
//                           labels: [
//                             "monday",
//                             "Tuesday",
//                             "Wednesday",
//                             "Thursday",
//                             "Friday",
//                             "Saturday",
//                             "Sunday",
//                           ],
//                           datasets: [
//                             {
//                               label: "Weekly Budget",
//                               data: [
//                                 monday_expense_amount,
//                                 tuesday_expense_amount,
//                                 wednesday_expense_amount,
//                                 thursday_expense_amount,
//                                 friday_expense_amount,
//                                 saturday_expense_amount,
//                                 sunday_expense_amount,
//                               ],
//                               backgroundColor: [
//                                 "#f56954",
//                                 "#00a65a",
//                                 "#f39c12",
//                                 "#00c0ef",
//                                 "#3c8dbc",
//                                 "#d2d6de",
//                               ],
//                               barThickness: 0.5
//                             },
//                           ],
//                           Options: {},
//                         },
                        
//                   });
//             },
        
//           //chart end here
//         });
//       });
//   }      
// })