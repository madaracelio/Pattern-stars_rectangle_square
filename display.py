import argparse
from Cone import Cone
from Rectangle import Rectangle
from SigmaSymbol import InvertedSigma, Sigma
from Stars import Complete_stars
from Triangle import InvertedTriangle, Triangle
from WedgeSymbol import InvertedWedgeSymbol, WedgeSymbol

parser = argparse.ArgumentParser(description='Display a geometric shape using stars.')

parser.add_argument('--cone', type=int,
                    help='display a cone')
parser.add_argument('--cone_inv', type=int,
                    help='invert the displaying cone shape')

parser.add_argument('--length', type=int,
                    help='lenght of the rectangle')
parser.add_argument('--width', type=int,
                    help='width of the rectangle')
parser.add_argument('--rectangle',
                    help='display a rectangle')

parser.add_argument('--square', type=int,
                    help='display square shape')

parser.add_argument('--sigma', type=int,
                    help='display a triangle')
parser.add_argument('--sigma_inv', type=int,
                    help='invert the displaying shape')

parser.add_argument('--stars', type=int,
                    help='display a stars') 

parser.add_argument('--triangle', type=int,
                    help='display a triangle')
parser.add_argument('--triangle_inv', type=int,
                    help='invert the displaying triangle shape')

parser.add_argument('--wedge', type=int,
                    help='display a wedge mathematical symbol')
parser.add_argument('--wedge_inv', type=int,
                    help='invert the displaying wedge mathematical symbol')

# argument
args = parser.parse_args()


if args.cone:
    Cone.create_cone(args.cone)
    print("cone with dimension = ", args.cone)
if args.cone_inv:
    Cone.create_cone(args.cone_inv)
    print("inverted cone with dimension = ", args.cone_inv)
if args.rectangle:
    Rectangle.create_rectangle(args.length, args.width)
    print("rectangle : length and width = ", args.length, args.width)
if args.sigma:
    Sigma.create_sigma(args.sigma)
    print("Sigma symbol with dimension = ", args.sigma)
if args.sigma_inv:
    InvertedSigma.create_inverted_sigma(args.sigma_inv)
    print("inverted sigma symbol with dimension = ", args.sigma_inv)
if args.triangle:
    Triangle.create_triangle(args.triangle)
    print("triangle with dimension = ", args.triangle)
if args.triangle_inv:
    InvertedTriangle.create_inverted_triangle(args.triangle_inv)
    print("inverted triangle with dimension = ", args.triangle_inv)
if args.wedge:
    WedgeSymbol.create_wedge_symbol(args.wedge)
    print("wedge mathematical symbol with dimension = ", args.wedge)
if args.wedge_inv:
    InvertedWedgeSymbol.create_inverted_wedge_symbol(args.wedge_inv)
    print("inverted wedge mathematical symbol with dimension = ", args.wedge_inv)