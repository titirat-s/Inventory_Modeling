
<h1 id="inventory-modeling">Inventory modeling</h1>
<p>The project purpose is to establish inventory modeling to find minimum cost and conduct inventory simulation by using python perform selected model to make  decisions.</p>

<h2 id="table-of-contents">Table of contents</h2>
<ul>
<li><a href="#overview">Overview</a></li>
<li><a href="#conclusion">Conclusion</a></li>
<li><a href="#sample-result">Sample result</a></li>
<li><a href="#how-to-run">How to run</a></li>
</ul>

<h2 id="overview">Overview:</h2>
<p>This repository contain sample data in xlsx file and python code use to calculating inventory parameters and modeling inventory cost which include to simulating order and arrive schedule using calculated parameters. The goal of this project is to define best parameters with the impact if not perform it to making better decisions.</p>
<p><strong>Parameters include</strong>:</p>
<ul>
<li>Safety stock</li>
<li>Re-order point</li>
<li>Economic order quantity wtih discount model</li>
<li>What-if analysis (for modeling)</li>
</ul>
<p><strong>Note</strong>: The policy uses in this template is the re-order point with fixed order quantity with single product and single supplier</p>

<h2 id="conclusion">Conclusion</h2>
<p>This template was used to answering the questions about how many quantity and when should make an orders to optimize inventory level and cost. The results of the template can be used to make decisions about inventory planning and scheduling.</p>

<h2 id="sample-result">Sample result</h2>
<p>Result of running sample data with random variate leadtime</p>

<b>Sample of demand and leadtime</b>

<img src="https://github.com/titirat-s/Inventory_Modeling/blob/main/result_image/1_demand_plt.png" alt="Sample demand" width="300">      <img src="https://github.com/titirat-s/Inventory_Modeling/blob/main/result_image/2_leadtime_plt.png" alt="Sample leadtime" width="300">

<b>Cost modeling and model selection</b>

<sub>Modeling cost in each order quantity in one order to unviel minimum cost model and cost impact</sub>

<img src="https://github.com/titirat-s/Inventory_Modeling/blob/main/result_image/3_cost_model_plt.png" alt="Cost model" width="600">
<img src="https://github.com/titirat-s/Inventory_Modeling/blob/main/result_image/4_select_model.png" alt="Select cost model" width="600">

<b>Inventory simulation and result</b>

<sub>Calculating inventory performance metrics from simulation of inventory level within period</sub>

<img src="https://github.com/titirat-s/Inventory_Modeling/blob/main/result_image/5_inventory_simulation_plt.png" alt="Inventory level simulation" width="600">

<img src="https://github.com/titirat-s/Inventory_Modeling/blob/main/result_image/6_simulation_result.png" alt="Simulation result" width="300">  <img src="https://github.com/titirat-s/Inventory_Modeling/blob/main/result_image/7_schedule.png" alt="Scheduling" width="300">

<h2 id="how-to-run">How to run</h2>
<p>To run this project on local machine, need to install require packages</p>
<p><strong>Installation for Windows</strong></p>
<ol>
<li>Get files from repository and open folder with text editor (VS Code)</li>
<li>Create and activate <em>virtual environment</em> in terminal<br>
  
  Create environment name <em>inventory-model-env</em> --for first time<br>
  
  <code>python -m venv inventory-model-env</code><br>
  
  Activate environment<br>
  
  <code>.\inventory-model-env\Scripts\activate</code></li>

<li>Install requirement packages from <strong>requirements.txt</strong><br>
  
  <code>pip install -r requirements.txt</code></li>

<li>Run simulation in <strong>Case_modeling.ipynb</strong></li>
<li>Deactivate environment after running<br>
  
  <code>deactivate</code></li>
</ol>
<p>Learn more about <a href="https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-a-new-virtual-environment">virtual environment</a></p>

<blockquote>
<p>Written with <a href="https://stackedit.io/">StackEdit</a>.</p>
</blockquote>
