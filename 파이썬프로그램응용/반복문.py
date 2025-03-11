{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPpw3FPFEW8TiOVvIRg/ank",
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
        "<a href=\"https://colab.research.google.com/github/shinchangyoung/python-algorithm-solutions/blob/main/%ED%8C%8C%EC%9D%B4%EC%8D%AC%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%EC%9D%91%EC%9A%A9/%EB%B0%98%EB%B3%B5%EB%AC%B8.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "반복문"
      ],
      "metadata": {
        "id": "1OCwn9Rb_rCF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# for 반복문1\n",
        "test_list = ['one', 'two', 'three']\n",
        "for i in test_list:\n",
        "  x = i + '!'\n",
        "  print(x)\n",
        "print()\n",
        "\n",
        "test_list2 = [1,2,3,4,5]\n",
        "for i in test_list2:\n",
        "  x = i + 1\n",
        "  print(x)"
      ],
      "metadata": {
        "id": "IfkJWdVz_sk_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# for 반복문2\n",
        "number = 0\n",
        "for score in [90, 25, 67, 45, 93]:\n",
        "  number += 1\n",
        "\n",
        "  if score > 60:\n",
        "    print(\"%d번 학생은 합격입니다.\" % number)\n",
        "  else:\n",
        "    print(\"%d번 학생은 불합격입니다.\" % number)\n",
        "print()\n",
        "\n",
        "number = 0\n",
        "for score in [90, 25, 67, 45, 93]:\n",
        "    number += 1\n",
        "\n",
        "    if score > 70:\n",
        "        print(\"%d번 학생은 합격입니다. 점수: %d점\" % (number, score))\n",
        "    else:\n",
        "        print(\"%d번 학생은 불합격입니다. 점수: %d점\" % (number, score))\n"
      ],
      "metadata": {
        "id": "Z3F88hCoAO48"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# while 문\n",
        "i = 0\n",
        "while i < 5:\n",
        "  i += 1\n",
        "  print('*' * i)"
      ],
      "metadata": {
        "id": "xVXIYUWTAXg3"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}