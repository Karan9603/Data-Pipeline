# Streamlit

**Streamlit** is a platform used to develop simple front-end web applications to demonstrate your data projects. It can deploy machine learning models, algorithms, and has a vast array of nicely pre-styled components to build interactive data visualizations. No web development skills are necessary, you can implement their widgets entirely through Python, then deploy for free to their [Cloud Platform](https://streamlit.io/cloud).

You will need to [install](https://docs.streamlit.io/get-started/installation/anaconda-distribution) `streamlit` into your Anaconda project environment. If you cannot find the package through the search in Navigator, click the green arrow icon on your environment and open a terminal. Here, paste the `pip install streamlit` script.

Test if it has successfully installed by running `streamlit hello`.

Streamlit is very well [documented](https://docs.streamlit.io/get-started/fundamentals), with lots of clear explanations, examples, and tutorials. Let's start our first app and have a play with some of the [components](https://docs.streamlit.io/develop/api-reference).

To test locally, run `streamlit run filename.py` from your terminal.

## Deploy to Streamlit Cloud

It takes only a few clicks to deploy your app to the web! You'll need to change a few things in the file:

1. Environment variables will be entered into Streamlit, so you won't need to use `dotenv` and `os`. Where you access them in your code, follow the format `variable = st.secrets["VARIABLE"]` (this won't work for running the code locally!)

2. All imported packages will need to be included in [a file](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies) called `requirements.txt`. Name the dependencies, and make sure the file is in either the same folder as your streamlit app file, or at the root of your repository. (If you are using `psycopg`, you'll need to include both `psycopg` and `psycopg-binary`.)

3. From your [dashboard](https://share.streamlit.io/) click **Create app** and **Deploy a public app from GitHub**. Select the relevant repository, branch, and file. Here you can also customize the app URL.

4. Under **Advanced settings** you'll be able to customize the Python version, and add your environment variables into a [`secrets.toml` file](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) (you'll need to use quotations around your string variables.)

5. Click **Deploy** and watch your app go live! Open the link on different devices to appreciate Streamlit's responsive design!
