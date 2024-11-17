[Basic Concepts]
AM (At the Money): This refers to an option that has intrinsic value. For a call option, this means the current price of the underlying asset is at or very close to the strike price, while for a put option, the price of the asset is at or very close to the strike price. AM options are typically more expensive but are more likely to be profitable if the price moves in the direction of the option holder.

OTM (Out of the Money): This refers to an option that has no intrinsic value. For a call option, this means the current price of the underlying asset is below the strike price, while for a put option, the price of the asset is above the strike price. OTM options are typically cheaper but are less likely to be profitable unless the price moves in favor of the option holder before expiration.


Call Option: A call option gives the holder the right (but not the obligation) to buy the underlying asset (like a stock) at a specific price (the strike price) within a specified time period (before expiration). Traders typically buy call options when they expect the price of the underlying asset to rise. For example, if you think Nvidia stock will increase in price, you might buy a call option at a lower strike price to potentially profit from that price rise.

Put Option: A put option gives the holder the right (but not the obligation) to sell the underlying asset at a specific price within a specified time period. Traders buy put options when they expect the price of the asset to fall. For example, if you expect Nvidia stock to decline, buying a put option could allow you to sell it at a higher strike price and profit from the decrease.

In both cases, the buyer of the option pays a premium for this right, while the seller (writer) of the option receives the premium but is obligated to sell (in the case of calls) or buy (in the case of puts) the asset if the option is exercised.

===================================================
[Iron Condor]
An **Iron Condor** is a neutral options strategy designed to profit from low volatility when a stock is expected to trade within a specific price range by expiration. It involves selling an out-of-the-money (OTM) put spread and an out-of-the-money call spread simultaneously, creating a **net credit** position. This strategy has defined maximum risk and reward, making it popular among options traders who want to generate income in a range-bound market.

### Refined Breakdown of the Iron Condor:

#### Key Characteristics:
- **Risk/Reward**: Limited risk and limited reward.
- **Profit Target**: Ideally, the stock remains between the short put and short call strike prices at expiration.
- **Neutral Strategy**: Suitable when you expect low volatility and believe the stock will not make significant price moves in either direction.
- **Net Credit**: The strategy generates a net credit upfront, which is the maximum profit if the stock remains within the desired range.
- **Defined Loss**: The maximum loss occurs if the stock price moves significantly beyond the sold strikes, and it's capped by the purchased options (the long put and long call).

#### Setup:
1. **Sell an OTM Put** (Higher Strike)  
   → Generates premium; obligates you to buy the asset if the price falls below this strike.
2. **Buy an OTM Put** (Lower Strike)  
   → Limits your risk on the downside if the stock falls too far.
3. **Sell an OTM Call** (Lower Strike)  
   → Generates premium; obligates you to sell the asset if the price rises above this strike.
4. **Buy an OTM Call** (Higher Strike)  
   → Limits your risk on the upside if the stock rises too far.

### Example:
Assume you are trading **Nvidia (NVDA)**, currently priced at $500, and you believe the price will remain between $490 and $510 over the next month. You can set up an Iron Condor as follows:

- **Sell a 490 put** and receive $5 in premium.
- **Buy a 480 put** and pay $3 in premium.
  
  → This forms a **bull put spread**, with a net credit of $2 (5 - 3).

- **Sell a 510 call** and receive $4 in premium.
- **Buy a 520 call** and pay $2 in premium.
  
  → This forms a **bear call spread**, with a net credit of $2 (4 - 2).

- **Total net credit**: $4 (2 from the put spread + 2 from the call spread).

### Key Scenarios:
1. **Maximum Profit**: 
   - If NVDA stays between $490 and $510 by expiration, all options expire worthless, and you keep the full $4 net credit.
   
2. **Maximum Loss**:
   - If NVDA moves beyond either $480 (on the downside) or $520 (on the upside), you will experience the maximum loss.
   - The loss is capped by the difference between the strike prices of the spreads (10 points) minus the premium received ($4), so **max loss = 10 - 4 = $6 per share**.

3. **Breakeven Points**:
   - On the downside: $490 (short put strike) - $4 (net credit) = **$486**.
   - On the upside: $510 (short call strike) + $4 (net credit) = **$514**.
   - If NVDA closes between $486 and $514, you still make a profit.

### Advantages of Iron Condor:
- **Profit from Stability**: If the stock stays within a range and doesn't make big moves, you keep the premium.
- **Defined Risk**: The risk is limited to the difference in strike prices minus the net credit received.
- **Flexibility**: You can adjust the strikes based on your volatility outlook or market conditions to widen or narrow the range of profitability.

### Disadvantages:
- **Risk of Large Losses**: If the stock moves significantly outside the desired range, you can incur the maximum loss.
- **Low Profit Potential**: While the risk is limited, so is the potential reward, and the strategy can have low returns in exchange for limited risk.
- **Volatility Sensitivity**: A sudden increase in volatility could push the stock price outside the range, leading to losses.

### Summary:
An Iron Condor is a great strategy for traders who expect **low volatility** and want to **profit from time decay** as the stock trades within a defined range. The **maximum profit** is the **net credit** received when initiating the trade, while the **maximum loss** is limited to the difference between the strike prices of the spreads, reduced by the credit. This strategy is well-suited for range-bound markets where dramatic price movements are unlikely.
===================================================
[Job Description]
The trade needs to be executed in ThinkOrSwim - the software I use for trading.
I am interested in options for anything in my Scan tab, but let's focus on the SPX, SPY, NDX, and QQQ. The scan tab idea will come later in future work.
I am looking for you to find the right strike price to set up an Iron Condor - I am going to give you a formula below - but then you pick the correct strikes and do a setup far Out of the money (OTM)
I have been doing 1% of the current price. So, I would need a button to click to have your code take action on that price showing in the ThinkOrSwim program.
Using the formula, 1% of the current price would have been 202 for NDX or 58 for SPX. I wasn't tracking the others today, but you would do this for all four indexes, one at a time. I would choose the Symbol and click your button.
Later on, we'll discuss more automation around Dec 2024 or sooner
I will have more than one of the ThinkOrSwim programs running simultaneously. For our testing, we'll use Paper Money.
Another thing to look for is to get as close as possible to Delta -.10 for Puts and Delta +.10 for Calls. It doesn't have to be precisely -.10 for Puts and +.10 for Calls, but close enough. I am interested in the 0 DTE for daily option trading for the four indexes. Later on, we'll do weekly symbols located in my scan tab, but not right now.
Once you determine the strikes for the trade, set up the Iron Condor.
Today, I set up 5870/5875/5815/5810. I picked these manually for SPX.
I want to specify the number of contracts I am interested in. Larger requests are more complex to fill; I would need them broken down into several setups. I could also go to the Monitor and click duplicate trade, but if you can set up multiples if I click another button, that would be faster since I would want to put them in close to the same time.

We are not placing real money or paper money trades. But the API should add the trades into the Analyze tab, and I will review and execute them myself (at least initially). If I enter qty 91, you need to break it into pieces and submit multiples to the Analyze tab. So you might have 45 in one and 46 in another, or let me specify how many pieces you have to break them up into or the maximum size per send. I'll send them throughout the day as I trade more in qty. I will send them manually fast/quickly, but smaller trades are easier for the broker to fill. I found when I run in paper mode, it fills immediately, so that is not a good test for the real market.

I don't exit the trades they are options and just expire, but they are sooooo far OTM that it should never cash out.

===================================================
[Other Requirements]

Will you be able to plug it into the ThinkOrSwim program, or will you use the API? It is important to me that I can see the results of the ThinkOrSwim program.
Please use C# and make a console to implement a backend.
With that, I can run it as a one-liner in the command window, with spaces between each parameter.
I need the API and other settings config files that I can change without having to recompile.
After I review the code in its final stage, I will make the final executable here.

===================================================
[Reference]

https://www.reddit.com/r/Schwab/comments/1c2ioe1/the_unofficial_guide_to_charles_schwabs_trader/
https://github.com/TreyThomas93/python-trading-bot-with-thinkorswim

===================================================
[Schwab API info]
App Key: iVm16EvmauKNKwHjvLbocVjhiH5cbabA
Secret: wjMGYDHoMXCySAni

===================================================
[Plan]
Here's a structured plan for implementing the Iron Condor trading automation using the Schwab Trader API:

### **Phase 1: Project Setup**
1. **Define Requirements:**
   - Automate Iron Condor trading for SPX, SPY, NDX, and QQQ.
   - Use Schwab Trader API for trading actions.
   - Set up trades with specific criteria (1% OTM, Delta around -0.10 for puts and +0.10 for calls).
   - Allow the user to specify the number of contracts.
   - Ensure compatibility with Paper Money for testing.

2. **Setup Development Environment:**
   - Install Python and required libraries (`requests` for HTTP requests).
   - Create a Schwab Developer account and register an application to obtain API credentials.
   - Set up a version control system (e.g., GitHub) for code management.

### **Phase 2: API Integration**
1. **OAuth Authentication Setup (1-2 Days):**
   - Implement the OAuth 2.0 flow to authenticate and retrieve an access token.
   - Write a script to automate this process, storing the access token securely.
   - Test access to the Schwab API to ensure successful authentication.

2. **Fetch Real-Time Market Data (1-2 Days):**
   - Develop a function to retrieve the latest prices for SPX, SPY, NDX, and QQQ.
   - Test the function to ensure data accuracy.

3. **Options Data Retrieval (2-3 Days):**
   - Implement functionality to fetch options chain data for specified symbols and expiration dates.
   - Parse the data to identify relevant information (strike prices, Delta values).
   - Write unit tests to validate data retrieval and parsing.

### **Phase 3: Iron Condor Setup**
1. **Calculate 1% OTM Levels (1 Day):**
   - Implement a function that calculates the target OTM levels based on 1% of the current price.

2. **Determine Strike Prices Based on Delta (2-3 Days):**
   - Develop a logic to find strike prices closest to the Delta criteria (-0.10 for puts and +0.10 for calls).
   - Create a function to construct the Iron Condor setup with calculated strikes.
   - Perform tests to validate that the calculated strikes meet the criteria.

3. **Automate the Trade Setup (2-3 Days):**
   - Implement the logic to set up the Iron Condor order using the Schwab API.
   - Add support for specifying the number of contracts.
   - Include error handling to manage potential issues during order submission.
   - Test the automation in the Paper Money environment.

### **Phase 4: User Interface and Interaction**
1. **Add Command-Line Interface (CLI) (2 Days):**
   - Create a CLI to allow the user to input the symbol, number of contracts, and start the automation process.
   - Provide feedback on the status of trades (successful, pending, or failed).

2. **Build Optional Graphical User Interface (GUI) (3-5 Days):**
   - Optionally, use a GUI library like `Tkinter` or `PyQt` to build a simple interface for user interactions.
   - Include buttons for selecting symbols, specifying the number of contracts, and initiating the trade.

### **Phase 5: Testing and Optimization**
1. **Extensive Testing with Paper Money (5-7 Days):**
   - Test different scenarios, including varying OTM levels and Delta values.
   - Run the script simultaneously in multiple instances of ThinkOrSwim.
   - Ensure the script handles API rate limits and network issues.

2. **Performance Optimization (2-3 Days):**
   - Optimize the script to handle larger trade requests by breaking them into smaller batches if needed.
   - Implement logging and monitoring for tracking trades and debugging.

### **Phase 6: Future Enhancements (Post-December 2024)**
1. **Expand to Weekly Symbols in the Scan Tab:**
   - Add support for scanning weekly symbols.
   - Implement logic for more sophisticated screening and filtering of potential trades.

2. **Full Automation and Monitoring:**
   - Develop a more automated monitoring system to track positions and perform adjustments.
   - Implement alerts and notifications for critical events.

### **Estimated Timeline**
- **Phase 1-3 (Core Features):** 3 weeks.
- **Phase 4 (User Interface):** 1 weeks.
- **Phase 5 (Testing & Optimization):** 2 weeks.
- **Phase 6 (Future Enhancements):** Post-December 2024.


===================================================
[Updated Plan]
The Schwab API is currently under development, so I'm not sure if it will support ThinkOrSwim trading. So I came up with an alternative method.
Using the Schwab API for historical data and AutoHotkey for trade execution provides a good balance between reliable data access and automated interaction with ThinkOrSwim. Let's break down this approach:

1. **Schwab API for Historical Data**
   - The Schwab API (currently in development) should provide access to historical market data.
   - This will give you reliable, programmatic access to the data needed for your Iron Condor strategy calculations.

2. **AutoHotkey for Trade Execution**
   - AutoHotkey will be used to automate the trade execution process.
   - This will allow you to interact with ThinkOrSwim programmatically, including clicking buttons and entering trade details.

Here's a revised plan incorporating these elements:
   
1. **Schwab API Integration**
   - Monitor the Schwab API development and sign up for early access if possible.
   - Once available, implement C# classes to authenticate and interact with the Schwab API.
   - Create methods to fetch historical data for SPX, SPY, NDX, and QQQ.
   - Implement data parsing and storage mechanisms.
2. **Iron Condor Strategy Implementation**
   - Develop the core logic for Iron Condor setup in C#.
   - Use the historical data from the Schwab API to inform your strategy (e.g., volatility calculations, trend analysis).
   - Implement the logic to calculate strike prices based on 1% OTM levels and Delta criteria.
   - Create methods to construct the Iron Condor setup and submit trades through the Schwab API.
3. **AutoHotkey for Trade Execution**
   - Develop AutoHotkey scripts to interact with ThinkOrSwim programmatically.
   - Ensure that the scripts can handle errors gracefully and provide feedback to the user.
   - Implement functions for:
     - Navigating to the Analyze tab
     - Submitting trades for analysis
     - Entering trade details (strikes, expiration, number of contracts)
4. **User Interface and Interaction**
   - Build a C# console application as the main interface.
   - Allow users to initiate data fetching, strategy calculation, and trade setup.
   - Provide feedback on the status of trades and any errors encountered.
6. **Configuration and Settings**
   - Create configuration files for API settings, AutoHotkey paths, and strategy parameters.
   - Implement a settings manager in C# to handle these configurations.
7. **Logging and Error Handling**
   - Implement robust logging for both the C# application and AutoHotkey scripts.
   - Develop error handling mechanisms, especially for AutoHotkey interactions which may be sensitive to UI changes.
8. **Testing and Validation**
   - Thoroughly test the Schwab API integration once available.
   - Conduct extensive testing of AutoHotkey scripts under various ThinkOrSwim UI states.
   - Perform end-to-end testing of the entire workflow.
9. **Documentation and User Guide**
   - Create detailed documentation on setting up and using the system.
   - Include troubleshooting guides, especially for AutoHotkey-related issues.
10. **Maintenance Plan**
    - Develop a strategy for keeping AutoHotkey scripts updated with any ThinkOrSwim UI changes.
    - Plan for regular updates to incorporate any changes in the Schwab API.
This approach leverages the reliability of official API data while using automation to interact with ThinkOrSwim. It's a good compromise given the current limitations.
I'll need to stay informed about the Schwab API development and I'll integrate it once it becomes available.

==========================
[Performance]
Once the application is approved, we need to get the first batch of authentication tokens.
In order to get authentication token, I developed python code.
But, I need Charles Schwab portfolio credentials now.
