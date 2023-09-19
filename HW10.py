{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPvD/oYcuxp5rjRMreLA6hN",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/XrommoZerG/GitInstructionWorkshop_2023-06-04/blob/main/HW10.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZN08Q2J0OWYl",
        "outputId": "aa7cd83d-f21d-48d4-f81f-c781277df230"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   whoAmI\n",
            "0   robot\n",
            "1   robot\n",
            "2   robot\n",
            "3   robot\n",
            "4   human\n",
            "5   robot\n",
            "6   human\n",
            "7   human\n",
            "8   human\n",
            "9   human\n",
            "10  robot\n",
            "11  robot\n",
            "12  human\n",
            "13  robot\n",
            "14  human\n",
            "15  human\n",
            "16  human\n",
            "17  human\n",
            "18  robot\n",
            "19  robot\n",
            "\n",
            "    human  robot\n",
            "0       0      1\n",
            "1       0      1\n",
            "2       0      1\n",
            "3       0      1\n",
            "4       1      0\n",
            "5       0      1\n",
            "6       1      0\n",
            "7       1      0\n",
            "8       1      0\n",
            "9       1      0\n",
            "10      0      1\n",
            "11      0      1\n",
            "12      1      0\n",
            "13      0      1\n",
            "14      1      0\n",
            "15      1      0\n",
            "16      1      0\n",
            "17      1      0\n",
            "18      0      1\n",
            "19      0      1\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import random\n",
        "\n",
        "lst = ['robot'] * 10\n",
        "lst += ['human'] * 10\n",
        "random.shuffle(lst)\n",
        "data = pd.DataFrame({'whoAmI': lst})\n",
        "print(data)\n",
        "\n",
        "print('')\n",
        "\n",
        "data['tmp'] = 1\n",
        "data.set_index([data.index, 'whoAmI'], inplace=True)\n",
        "data = data.unstack(level=-1, fill_value = 0).astype(int)\n",
        "data.columns = data.columns.droplevel()\n",
        "data.columns.name = None\n",
        "print(data)"
      ]
    }
  ]
}